import pandas as pd

# Create Sales DataFrame
data = {
        "OrderID": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010,
                1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020],

        "Date": ["2025-01-05", "2025-01-06", "2025-01-07", "2025-01-08", "2025-01-09",
                "2025-01-10", "2025-01-11", "2025-01-12", "2025-01-13", "2025-01-14",
                "2025-01-15", "2025-01-16", "2025-01-17", "2025-01-18", "2025-01-19",
                "2025-01-20", "2025-01-21", "2025-01-22", "2025-01-23", "2025-01-24"],

        "Region": ["East", "West", "North", "South", "East",
                "West", "North", "South", "East", "West",
                "North", "South", "East", "West", "North",
                "South", "East", "West", "North", "South"],
                
        "Product": ["Laptop", "Tablet", "Laptop", "Phone", "Tablet",
                "Laptop", "Phone", "Tablet", "Phone", "Laptop",
                "Tablet", "Laptop", "Phone", "Tablet", "Laptop",
                "Phone", "Laptop", "Phone", "Tablet", "Laptop"],

        "Quantity": [2, 5, 3, 10, 7, 1, 6, 4, 8, 4,
                9, 3, 12, 6, 5, 7, 3, 10, 2, 6],

        "UnitPrice": [600, 300, 600, 200, 300, 600, 200, 300, 200, 600,
                        300, 600, 200, 300, 600, 200, 600, 200, 300, 600],

        "SalesPerson": ["John", "Alice", "Mike", "Emma", "John",
                        "Alice", "Mike", "Emma", "John", "Alice",
                        "Mike", "Emma", "John", "Alice", "Mike",
                        "Emma", "John", "Alice", "Mike", "Emma"]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)
print(df.head(10))
print(df.tail(10))
print(df.describe())

# Add TotalSales column (Quantity * UnitPrice)
df["TotalSales"] = df["Quantity"] * df["UnitPrice"]
print(df)

# Total Revenue
total_revenue = df["TotalSales"].sum()
print("\n Total Revenue: ", total_revenue)

# Revenue by product
revenue_by_product = df.groupby("Product")["TotalSales"].sum().sort_values(ascending=False)
print("\n Revenue by Product:\n", revenue_by_product)

# Top Revenue Product
top_product = revenue_by_product.idxmax()
print("\n Top Revenue Product:", top_product)

# LOW Revenue product
low_product = revenue_by_product.idxmin()
print("\n low Revenue Product\n :", low_product)

# Revenue by Region
revenue_by_region = df.groupby("Region")["TotalSales"].sum().sort_values(ascending=False)
print("\n Revenue by Region:\n", revenue_by_region)

# Top Revenue Region
top_region = revenue_by_region.idxmax()
print("\n Top Revenue Region:", top_region)

# Revenue by SalesPerson
revenue_by_salesperson = df.groupby("SalesPerson")["TotalSales"].sum().sort_values(ascending=False)
print("\n Revenue by SalesPerson:\n", revenue_by_salesperson)

# Average Order Value
aov = df["TotalSales"].mean().round(2)
print("\n Average Order Value:", aov)

# Units Sold by Region
units_by_region = df.groupby("Region")["Quantity"].sum().sort_values(ascending=False)
print("\n Units Sold by Region:\n", units_by_region)

# Top SalesPerson
top_salesperson = revenue_by_salesperson.idxmax()
print("\n Top SalesPerson by Revenue:", top_salesperson)