import pandas as pd
from pathlib import Path

# Find the main project folder
project_folder = Path(__file__).resolve().parent.parent

visualizations_folder = project_folder / "visualizations"
visualizations_folder.mkdir(exist_ok=True)

# Find the CSV file
data_file = project_folder / "data" / "ecommerce_events.csv"

# Load the dataset
df = pd.read_csv(data_file)

# Show the first 5 records
print("First 5 records:")
print(df.head())

# Show the dataset size
print("\nDataset shape:")
print(df.shape)

# Show all column names
print("\nColumn names:")
print(df.columns.tolist())

event_counts = df["event_type"].value_counts()

print("\nEvent counts:")
print(event_counts)

view_to_cart = (1211 / 3066) * 100
cart_to_purchase = (723 / 1211) * 100

print("\nFunnel rates:")
print("View to Cart:", round(view_to_cart, 2), "%")
print("Cart to Purchase:", round(cart_to_purchase, 2), "%")

customer_funnel = df.groupby("event_type")["customer_id"].nunique()

print("\nUnique customers by event type:")
print(customer_funnel)

# Customer-level funnel

view_customers = set(df[df["event_type"] == "view"]["customer_id"])
cart_customers = set(df[df["event_type"] == "cart"]["customer_id"])
purchase_customers = set(df[df["event_type"] == "purchase"]["customer_id"])

view_and_cart = view_customers & cart_customers
view_cart_purchase = view_customers & cart_customers & purchase_customers

print("\nCustomer Funnel:")
print("Customers who viewed:", len(view_customers))
print("Customers who viewed and added to cart:", len(view_and_cart))
print("Customers who viewed, carted and purchased:", len(view_cart_purchase))

view_to_cart_customers = (len(view_and_cart) / len(view_customers)) * 100
cart_to_purchase_customers = (len(view_cart_purchase) / len(view_and_cart)) * 100
view_to_purchase_customers = (len(view_cart_purchase) / len(view_customers)) * 100

print("\nCustomer Funnel Conversion Rates:")
print("View to Cart:", round(view_to_cart_customers, 2), "%")
print("Cart to Purchase:", round(cart_to_purchase_customers, 2), "%")
print("View to Purchase:", round(view_to_purchase_customers, 2), "%")

# How much revenue did the e-commerce business generate, and which product categories generated the most revenue?
total_revenue = df["revenue"].sum()

print("\nTotal Revenue:")
print("R", round(total_revenue, 2))

#Which product categories generated the most revenue?
revenue_by_category = df.groupby("product_category")["revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Product Category:")
print(revenue_by_category)

#Which countries are generating the most revenue?
revenue_by_country = df.groupby("country")["revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Country:")
print(revenue_by_country)

#Do Mobile, Desktop, and Tablet users generate different amounts of revenue?
revenue_by_device = df.groupby("device")["revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Device:")
print(revenue_by_device)

customers_by_device = df.groupby("device")["customer_id"].nunique().sort_values(ascending=False)

print("\nUnique Customers by Device:")
print(customers_by_device)
#Revenue per customer
revenue_per_customer = (
    df.groupby("device")["revenue"].sum()
    / df.groupby("device")["customer_id"].nunique()
)

print("\nRevenue per Customer by Device:")
print(revenue_per_customer.round(2))

df["event_date"] = pd.to_datetime(df["event_date"])

monthly_revenue = df.groupby(
    df["event_date"].dt.to_period("M")
)["revenue"].sum()

print("\nMonthly Revenue:")
print(monthly_revenue)

#Purchases by Product Category

purchases_by_category = (
    df[df["event_type"] == "purchase"]
    .groupby("product_category")
    .size()
    .sort_values(ascending=False)
)

print("\nPurchases by Product Category:")
print(purchases_by_category)

#Average Purchase Value by Category

average_purchase_value = (
    df[df["event_type"] == "purchase"]
    .groupby("product_category")["revenue"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Purchase Value by Category:")
print(average_purchase_value.round(2))

#Top 10 Customers by Revenue

top_customers = (
    df.groupby("customer_id")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Customers by Revenue:")
print(top_customers)

#Customer Purchase Analysis

purchasing_customers = df[df["event_type"] == "purchase"]["customer_id"].nunique()

total_customers = df["customer_id"].nunique()

print("\nCustomer Purchase Analysis:")
print("Total unique customers:", total_customers)
print("Customers who purchased:", purchasing_customers)

#Customer Purchase Rate

purchase_rate = (purchasing_customers / total_customers) * 100

print("\nCustomer Purchase Rate:")
print(round(purchase_rate, 2), "%")

#Repeat Customer Analysis

purchase_counts = (
    df[df["event_type"] == "purchase"]
    .groupby("customer_id")
    .size()
)

repeat_customers = (purchase_counts > 1).sum()

print("\nRepeat Customer Analysis:")
print("Customers with at least one purchase:", len(purchase_counts))
print("Repeat customers:", repeat_customers)

#Repeat Customer Rate

repeat_customer_rate = (repeat_customers / len(purchase_counts)) * 100

print("\nRepeat Customer Rate:")
print(round(repeat_customer_rate, 2), "%")

#Purchase Frequency

purchase_frequency = purchase_counts.value_counts().sort_index()

print("\nPurchase Frequency:")
print(purchase_frequency)

#Monthly Revenue Chart

import matplotlib.pyplot as plt

# Monthly Revenue Chart

import matplotlib.pyplot as plt

monthly_revenue_chart = monthly_revenue.copy()
monthly_revenue_chart.index = monthly_revenue_chart.index.astype(str)

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_revenue_chart.index,
    monthly_revenue_chart.values,
    marker="o"
)

plt.title("Monthly Purchase Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (R)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    visualizations_folder / "monthly_revenue.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

#Revenue by Product Category Chart

plt.figure(figsize=(10, 5))

plt.bar(
    revenue_by_category.index,
    revenue_by_category.values
)

plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue (R)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    visualizations_folder / "revenue_by_category.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

#Revenue by Device Chart

plt.figure(figsize=(8, 5))

plt.bar(
    revenue_by_device.index,
    revenue_by_device.values
)

plt.title("Revenue by Device")
plt.xlabel("Device")
plt.ylabel("Revenue (R)")
plt.tight_layout()

plt.savefig(
    visualizations_folder / "revenue_by_device.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

#Top 10 Customers by Revenue Chart

plt.figure(figsize=(10, 6))

plt.barh(
    top_customers.index,
    top_customers.values
)

plt.title("Top 10 Customers by Purchase Revenue")
plt.xlabel("Revenue (R)")
plt.ylabel("Customer ID")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig(
    visualizations_folder / "top_10_customers.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

#Average Purchase Value by Category Chart

plt.figure(figsize=(10, 5))

plt.bar(
    average_purchase_value.index,
    average_purchase_value.values
)

plt.title("Average Purchase Value by Category")
plt.xlabel("Product Category")
plt.ylabel("Average Purchase Value (R)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    visualizations_folder / "average_purchase_value_by_category.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()