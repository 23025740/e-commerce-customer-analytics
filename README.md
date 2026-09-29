# E-commerce Customer Analytics

## Project Overview

This project analyzes simulated e-commerce customer activity and purchase data to identify patterns in customer behavior, revenue, product categories, devices, countries, and purchasing frequency.

The analysis was performed using Python, Pandas, SQL Server, and Matplotlib.

## Objectives

* Analyze customer purchasing behavior
* Identify revenue patterns across product categories
* Compare revenue across devices and countries
* Analyze monthly purchase revenue
* Identify high-value customers
* Calculate customer purchase and repeat-customer metrics
* Demonstrate the same analysis using both Python and SQL

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* SQL Server
* SQL Server Management Studio (SSMS)
* Git and GitHub

## Dataset

The dataset contains 5,000 simulated e-commerce events.

The dataset includes:

* Event ID
* Customer ID
* Event date
* Event type
* Product ID
* Product category
* Quantity
* Unit price
* Device
* Country
* Revenue

Event types include:

* View
* Cart
* Purchase

Revenue is calculated only for purchase events.

> Note: The dataset is synthetic and was generated for portfolio and learning purposes. It does not represent real customer or business data.

## Key Analysis

### Customer Purchase Rate

* Total unique customers: 989
* Customers who purchased: 514
* Customer purchase rate: 51.97%

### Repeat Customers

* Purchasing customers: 514
* Repeat customers: 163
* Repeat customer rate: 31.71%

### Total Purchase Revenue

**R1,494,298**

### Revenue by Product Category

| Product Category |  Revenue |
| ---------------- | -------: |
| Beauty           | R349,598 |
| Clothing         | R312,054 |
| Sports           | R286,738 |
| Electronics      | R274,809 |
| Home & Kitchen   | R271,099 |

### Revenue by Device

| Device  |  Revenue |
| ------- | -------: |
| Mobile  | R507,072 |
| Desktop | R497,757 |
| Tablet  | R489,469 |

### Revenue by Country

| Country      |  Revenue |
| ------------ | -------: |
| Kenya        | R345,048 |
| South Africa | R330,931 |
| Ghana        | R285,694 |
| Nigeria      | R281,984 |
| Botswana     | R250,641 |

### Monthly Revenue

The highest recorded monthly purchase revenue occurred in **July 2026**, at **R248,090**.

## Visualizations

The project includes the following visualizations:

* Monthly purchase revenue
* Revenue by product category
* Revenue by device
* Top 10 customers by purchase revenue
* Average purchase value by category

The charts are stored in the `visualizations` folder.

## SQL Analysis

SQL Server was used to reproduce the Python analysis and demonstrate:

* Filtering with `WHERE`
* Aggregation using `SUM()`, `COUNT()`, and `AVG()`
* Grouping using `GROUP BY`
* Sorting using `ORDER BY`
* Customer-level analysis using `DISTINCT`
* Conditional aggregation using `CASE`
* Subqueries
* Top-N analysis using `TOP`

The SQL queries are available in:

`sql/ecommerce_analysis.sql`

## Python Analysis

The Python analysis is available in:

`notebook/ecommerce_analysis.py`

The dataset generation script is available in:

`Generate_data.py`

## Project Structure

```text
E_commerce_sales
│
├── data
│   └── ecommerce_events.csv
│
├── notebook
│   └── ecommerce_analysis.py
│
├── sql
│   └── ecommerce_analysis.sql
│
├── visualizations
│   ├── monthly_revenue.png
│   ├── revenue_by_category.png
│   ├── revenue_by_device.png
│   ├── top_10_customers.png
│   └── average_purchase_value_by_category.png
│
├── Generate_data.py
└── README.md
```

## How to Run

### Generate the dataset

```bash
python Generate_data.py
```

### Run the Python analysis

```bash
python notebook/ecommerce_analysis.py
```

### Run the SQL analysis

Open `sql/ecommerce_analysis.sql` in SQL Server Management Studio and execute the queries against the `ECommerceAnalytics` database.

# Skills Demonstrated

This project demonstrates practical experience in:

* Data cleaning and preparation
* Exploratory data analysis
* Customer analytics
* Revenue analysis
* Data aggregation
* Business-focused insights
* Python/Pandas
* SQL
* Data visualization
* Working with relational databases
* Documenting an analytics project

# Future Improvements

* Build a more realistic customer journey and session-based funnel
* Add a dashboard using Power BI or Streamlit
* Create a normalized relational database with customer and product tables
* Add more advanced customer segmentation
* Add automated data pipelines
* Deploy the analytics solution using Azure
