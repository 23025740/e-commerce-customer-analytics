import pandas as pd
import numpy as np
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).resolve().parent

# Create the data folder if it does not exist
data_folder = project_folder / "data"
data_folder.mkdir(exist_ok=True)

# Number of records we want to create
number_of_records = 5000

# Make the random data reproducible
np.random.seed(42)

# Possible values for our dataset
customers = [f"C{i}" for i in range(1001, 2001)]

products = [f"P{i}" for i in range(101, 201)]

categories = [
    "Electronics",
    "Clothing",
    "Home & Kitchen",
    "Beauty",
    "Sports"
]

event_types = [
    "view",
    "cart",
    "purchase"
]

devices = [
    "Mobile",
    "Desktop",
    "Tablet"
]

countries = [
    "South Africa",
    "Nigeria",
    "Kenya",
    "Ghana",
    "Botswana"
]

# Create the dataset
data = {
    "event_id": range(1, number_of_records + 1),

    "customer_id": np.random.choice(
        customers,
        number_of_records
    ),

    "event_date": pd.date_range(
        start="2026-01-01",
        end="2026-09-01",
        periods=number_of_records
    ),

    "event_type": np.random.choice(
        event_types,
        number_of_records,
        p=[0.60, 0.25, 0.15]
    ),

    "product_id": np.random.choice(
        products,
        number_of_records
    ),

    "product_category": np.random.choice(
        categories,
        number_of_records
    ),

    "quantity": np.random.randint(
        1,
        5,
        number_of_records
    ),

    "unit_price": np.random.choice(
        [99, 149, 249, 399, 599, 799, 999, 1499, 2499],
        number_of_records
    ),

    "device": np.random.choice(
        devices,
        number_of_records
    ),

    "country": np.random.choice(
        countries,
        number_of_records
    )
}

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data)

# Calculate revenue only for purchase events
df["revenue"] = np.where(
    df["event_type"] == "purchase",
    df["quantity"] * df["unit_price"],
    0
)

# Save the dataset
data_file = data_folder / "ecommerce_events.csv"
df.to_csv(data_file, index=False)

print("Dataset created successfully!")
print("Number of records:", len(df))

print("\nSaved to:")
print(data_file)

print("\nFirst 5 records:")
print(df.head())