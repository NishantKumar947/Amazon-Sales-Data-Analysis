import sys
import os

sys.path.append(os.path.dirname(__file__))

from data_cleaning import load_and_clean_data

# Load data
df = load_and_clean_data("data/Amazon Sale Report.csv")

print(df.head())
print(df.info())

# ================= BASIC METRICS =================
total_sales = df['Amount'].sum()
print("Total Sales:", total_sales)

total_orders = df['Order ID'].nunique()
print("Total Orders:", total_orders)

avg_order_value = total_sales / total_orders
print("Average Order Value:", avg_order_value)

# ================= CATEGORY ANALYSIS =================
print("\nTop Categories by Sales:")
print(df.groupby('Category')['Amount'].sum().sort_values(ascending=False).head())

# ================= STATE ANALYSIS =================
print("\nTop States by Sales:")
print(df.groupby('ship-state')['Amount'].sum().sort_values(ascending=False).head())

# ================= FULFILMENT =================
print("\nSales by Fulfilment:")
print(df.groupby('Fulfilment')['Amount'].sum())

# ================= STATUS =================
print("\nOrder Status Count:")
print(df['Status'].value_counts())

# ================= NEW ANALYSIS =================

# Cancellation Rate
cancel_count = df[df['Status'] == 'Cancelled'].shape[0]
cancel_rate = (cancel_count / total_orders) * 100
print("\nCancellation Rate:", cancel_rate)

# Cancellation by Category
print("\nCancellation by Category:")
cancel_data = df[df['Status'] == 'Cancelled']
print(cancel_data['Category'].value_counts().head())

# Sales Trend
print("\nSales Trend (first few rows):")
trend = df.groupby('Date')['Amount'].sum()
print(trend.head())