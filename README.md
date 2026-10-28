# Adidas US Sales Analytics

## 📊 Project Overview

This project analyzes Adidas US sales data to understand sales performance, profitability, customer-facing sales channels, retailers, products, and regional trends.

The project combines **Python, SQL, and Power BI** to take the dataset from raw data to a cleaned dataset, analytical queries, and an interactive dashboard.

The main goal was to answer practical business questions such as:

- Which products generate the most revenue and profit?
- Which retailers perform best?
- Which regions contribute the most to sales?
- Which sales methods perform better?
- How does operating margin vary across retailers and regions?
- Which product and sales-method combinations generate the highest revenue?

---

## 🛠️ Tools & Technologies

- **Python** – Data cleaning and validation
- **Pandas** – Data manipulation and analysis
- **SQLite** – Data storage and SQL analysis
- **SQL** – Business analysis and aggregations
- **Power BI** – Interactive dashboard and visualization
- **DAX** – Measures and profitability calculations
- **Git & GitHub** – Version control and project management

---

## 📁 Project Workflow

The project follows this workflow:

```text
Raw Adidas Sales Dataset
        ↓
Python Data Cleaning
        ↓
Data Validation
        ↓
Cleaned Dataset
        ↓
SQLite Database
        ↓
SQL Business Analysis
        ↓
Power BI
        ↓
Interactive Dashboard
        ↓
Business Insights
```

---

## 🧹 1. Data Cleaning with Python

The original dataset contained formatting issues, including unnecessary columns and header rows.

Python was used to clean and prepare the dataset for analysis.

### Cleaning steps included:

- Removed unnecessary columns
- Corrected the dataset header
- Removed empty rows
- Converted `Invoice Date` into a proper datetime format
- Converted numerical columns to appropriate data types
- Checked for missing values
- Checked for duplicate records
- Validated numerical values
- Checked for negative sales, units, prices, and operating profit
- Validated operating margin calculations
- Validated the relationship between price, units sold, and total sales

### Final dataset

The cleaned dataset contains:

- **9,648 records**
- **13 analytical columns**

Main columns include:

```text
Retailer
Retailer ID
Invoice Date
Region
State
City
Product
Price per Unit
Units Sold
Total Sales
Operating Profit
Operating Margin
Sales Method
```

---

## 🗄️ 2. SQLite Database

The cleaned dataset was loaded into a SQLite database to perform structured SQL analysis.

The database allows the sales data to be queried efficiently without repeatedly manipulating the raw CSV file.

---

## 🔎 3. SQL Analysis

SQL was used to answer business-oriented questions related to sales and profitability.

The analysis includes:

- Overall revenue and profit
- Revenue by region
- Revenue by retailer
- Revenue by product
- Revenue by sales method
- Monthly sales trends
- Operating margin analysis
- Retailer profitability ranking
- Product performance
- Sales-channel performance
- Top and lower-performing segments

The SQL queries are available in:

```text
sql/adidas_analysis.sql
```

---

## 📈 4. Power BI Dashboard

The cleaned data was imported into Power BI to create an interactive sales analytics dashboard.

### Dashboard analysis includes:

- Total Revenue
- Total Profit
- Total Units Sold
- Operating Margin
- Regional performance
- Retailer performance
- Product performance
- Sales method analysis
- Product profitability
- Retailer profitability ranking
- Region × Retailer profitability heatmap
- Revenue vs Operating Margin analysis

### Advanced analysis

The dashboard also includes:

- DAX measures
- Retailer profitability ranking
- Conditional formatting
- Interactive visual filtering
- Product × Sales Method analysis
- Revenue and profitability comparisons

---

## 📊 Dashboard Pages

### Page 1 — Sales Overview

The first page provides an overall view of Adidas US sales performance.

It focuses on:

- Revenue
- Profit
- Units Sold
- Regional performance
- Product performance
- Retailer performance
- Sales methods
- Overall sales trends

### Page 2 — Advanced Analytics

The second page focuses on deeper business analysis.

It includes:

- Product profitability analysis
- Product × Sales Method revenue analysis
- Operating margin comparisons
- Retailer and regional analysis
- Interactive filtering using slicers

---

## 💡 Key Business Questions

This project was designed around questions that a Data Analyst might receive from a business team:

1. Which products generate the highest revenue?
2. Which products are the most profitable?
3. Which retailers contribute the most sales?
4. Which regions perform best?
5. Which sales method generates the most revenue?
6. Which retailers have stronger operating margins?
7. Which product and sales-method combinations perform best?
8. Are high-revenue retailers also highly profitable?
9. How does profitability vary across regions and retailers?
10. What areas could potentially require further business attention?

---

## 🔬 Data Validation

Several validation checks were performed before analysis.

### Missing values

All analytical columns were checked for missing values.

### Duplicate records

Duplicate rows were checked and no duplicate records were found in the cleaned dataset.

### Negative values

The following were validated:

- Price per Unit
- Units Sold
- Total Sales
- Operating Profit

No negative values were found.

### Operating Margin

Operating margin values were validated against the underlying revenue and profit data.

### Sales Validation

The relationship between:

```text
Price per Unit × Units Sold
```

and:

```text
Total Sales
```

was also investigated to identify inconsistencies in the source data rather than silently modifying the original business values.

---

## 📂 Project Structure

```text
Adidas-US-Sales-Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── adidas_sales_cleaned.csv
│
├── sql/
│   └── adidas_analysis.sql
│
├── dashboard/
│   └── Adidas_US_Sales.pbix
│
├── clean_data.py
│
├── adidas.db
│
├── README.md
│
└── .gitignore
```

---

## 🚀 Skills Demonstrated

This project demonstrates practical skills in:

- Data Cleaning
- Data Validation
- Exploratory Data Analysis
- Python
- Pandas
- SQL
- SQLite
- Power BI
- DAX
- Data Visualization
- Dashboard Development
- Business Analysis
- Git & GitHub

---

## 🎯 Conclusion

This project demonstrates an end-to-end data analytics workflow, starting from a raw sales dataset and progressing through **data cleaning, validation, SQL analysis, DAX calculations, and interactive Power BI visualization**.

The main focus was not only on creating charts, but on using data to answer practical business questions around **sales, profitability, products, retailers, regions, and sales channels**.

---

