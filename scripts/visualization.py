import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(__file__))

from data_cleaning import load_and_clean_data

# Load data
df = load_and_clean_data("data/Amazon Sale Report.csv")

# ================= SALES TREND =================
trend = df.groupby('Date')['Amount'].sum()

plt.figure()
trend.plot()
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.savefig("outputs/charts/sales_trend.png")

# ================= CATEGORY SALES =================
category_sales = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)

plt.figure()
category_sales.head(5).plot(kind='bar')
plt.title("Top 5 Categories by Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.savefig("outputs/charts/category_sales.png")

# ================= STATE SALES =================
state_sales = df.groupby('ship-state')['Amount'].sum().sort_values(ascending=False)

plt.figure()
state_sales.head(5).plot(kind='bar')
plt.title("Top 5 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")
plt.savefig("outputs/charts/state_sales.png")

print("Charts saved in outputs/charts/")