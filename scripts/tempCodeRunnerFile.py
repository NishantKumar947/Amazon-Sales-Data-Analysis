# Total Sales
total_sales = df['Amount'].sum()
print("Total Sales:", total_sales)

# Total Orders
total_orders = df['Order ID'].nunique()
print("Total Orders:", total_orders)

# Average Order Value
avg_order_value = total_sales / total_orders
print("Average Order Value:", avg_order_value)