import pandas as pd

file_path = "data/raw/Adidas US Sales Datasets.xlsx"

df = pd.read_excel(file_path, header=4)

print("Dataset loaded successfully!")
print("Shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

df = df.drop(columns=['Unnamed: 0'])

print("\nColumns after cleaning:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)

print("\nDuplicate rows:", df.duplicated().sum())

print("\nUnique Regions:")
print(df["Region"].unique())

print("\nUnique Retailers:")
print(df["Retailer"].unique())

print("\nUnique Products:")
print(df["Product"].unique())

print("\nUnique Sales Methods:")
print(df["Sales Method"].unique())

print("\nNumeric validation:")

print("Negative Price per Unit:", (df["Price per Unit"] < 0).sum())
print("Negative Units Sold:", (df["Units Sold"] < 0).sum())
print("Negative Total Sales:", (df["Total Sales"] < 0).sum())
print("Negative Operating Profit:", (df["Operating Profit"] < 0).sum())

print("\nOperating Margin range:")
print("Minimum:", df["Operating Margin"].min())
print("Maximum:", df["Operating Margin"].max())

calculated_sales = df["Price per Unit"] * df["Units Sold"]

difference = (df["Total Sales"] - calculated_sales).abs()

print("\nSales calculation validation:")
print("Maximum difference:", difference.max())
print("Rows with difference:", (difference > 1).sum())

print("\nRows where calculated sales differs from Total Sales:")

check = df[[
    "Retailer",
    "Product",
    "Price per Unit",
    "Units Sold",
    "Total Sales"
]].copy()

check["Calculated Sales"] = check["Price per Unit"] * check["Units Sold"]

check["Difference"] = (
    check["Total Sales"] - check["Calculated Sales"]
).abs()

print(check[check["Difference"] > 1].head(10).to_string(index=False))

calculated_margin = df["Operating Profit"] / df["Total Sales"]

margin_difference = (
    df["Operating Margin"] - calculated_margin
).abs()

print("\nOperating margin validation:")
print("Maximum difference:", margin_difference.max())
print("Rows with difference:", (margin_difference > 0.001).sum())


output_path = "data/processed/adidas_sales_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print("Saved to:", output_path)