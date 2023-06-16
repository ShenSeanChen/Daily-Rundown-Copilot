


import pandas as pd

# Read the data from Excel
data = pd.read_csv("iMorning_test.csv")

# Calculate YoY growth rate for each item and vendor
data["YoY_Growth_Rate"] = ((data["Yesterday_Sales_ThisYear"] - data["Yesterday_Sales_LastYear"]) / data["Yesterday_Sales_LastYear"]) * 100

# Sort the data by YoY growth rate in descending order
sorted_data = data.sort_values(by="YoY_Growth_Rate", ascending=False)

# Generate the ranked list of top performing items and vendors
top_items = sorted_data.groupby("ITEM_NAME").first().sort_values(by="YoY_Growth_Rate", ascending=False)
top_vendors = sorted_data.groupby("VENDOR_NAME").first().sort_values(by="YoY_Growth_Rate", ascending=False)

# Print the insights
print("Top Performing Items (YoY Growth Rate):")
print(top_items[["YoY_Growth_Rate"]])

print("\nTop Performing Vendors (YoY Growth Rate):")
print(top_vendors[["YoY_Growth_Rate"]])




import pandas as pd

# Read the data from Excel
# data = pd.read_excel("sales_data.xlsx")

# Calculate YoY growth rate for each item and vendor
data["YoY_Growth_Rate"] = ((data["Yesterday_Sales_ThisYear"] - data["Yesterday_Sales_LastYear"]) / data["Yesterday_Sales_LastYear"]) * 100

# Sort the data by YoY growth rate in ascending order to find items/vendors not doing well
sorted_data = data.sort_values(by="YoY_Growth_Rate", ascending=True)

# Generate the ranked list of items/vendors not doing well
not_doing_well_items = sorted_data.groupby("ITEM_NAME").first().sort_values(by="YoY_Growth_Rate", ascending=True)
not_doing_well_vendors = sorted_data.groupby("VENDOR_NAME").first().sort_values(by="YoY_Growth_Rate", ascending=True)

# Print the items/vendors not doing well
print("Items Not Doing Well (YoY Growth Rate):")
print(not_doing_well_items[["YoY_Growth_Rate"]])

print("\nVendors Not Doing Well (YoY Growth Rate):")
print(not_doing_well_vendors[["YoY_Growth_Rate"]])

# Find the items with the highest price increase
data["Price_Increase"] = data["Yesterday_Sales_ThisYear"] - data["Yesterday_Sales_LastYear"]
top_price_increase_items = data.groupby("ITEM_NAME").sum().sort_values(by="Price_Increase", ascending=False)

# Calculate the effect of price increase on total sales units
total_sales_units = data["Yesterday_Units_ThisYear"].sum()
top_price_increase_items["Unit_Percentage_Change"] = (top_price_increase_items["Price_Increase"] / total_sales_units) * 100

# Print the items with the highest price increase and their effect on total sales units
print("\nItems with Highest Price Increase:")
print(top_price_increase_items[["Price_Increase", "Unit_Percentage_Change"]])

# Recommendations for the future assortment plan
print("\nRecommendations for Future Assortment Plan:")
print("1. Focus on the top performing items and vendors with high YoY growth rates.")
print("2. Identify and address the issues with items and vendors that are not doing well.")
print("3. Monitor price changes and their impact on total sales units.")
print("4. Consider expanding or introducing new items from top performing vendors.")
print("5. Conduct market research and customer surveys to identify emerging trends and preferences.")


# First Attempt

# import pandas as pd

# # Load the sales data into a DataFrame
# data = pd.read_csv('iMorning_test.csv')

# # Calculate the year-over-year (YoY) growth rate for each item
# data['YoY_Growth_Rate'] = ((data['Yesterday_Sales_ThisYear'] - data['Yesterday_Sales_LastYear']) / data['Yesterday_Sales_LastYear']) * 100

# # Top Performing Items (YoY)
# top_performing_items = data.sort_values(by='YoY_Growth_Rate', ascending=False)
# print("Top Performing Items (YoY):")
# print(top_performing_items[['ITEM_NAME', 'YoY_Growth_Rate']].head())

# # Top Performing Vendors (YoY)
# top_performing_vendors = data.groupby('VENDOR_NAME')['YoY_Growth_Rate'].sum().reset_index()
# top_performing_vendors = top_performing_vendors.sort_values(by='YoY_Growth_Rate', ascending=False)
# print("\nTop Performing Vendors (YoY):")
# print(top_performing_vendors.head())

# # Items Not Performing Well (YoY)
# items_not_performing = data[data['YoY_Growth_Rate'] <= 0]
# items_not_performing = items_not_performing.sort_values(by='YoY_Growth_Rate')
# print("\nItems Not Performing Well (YoY):")
# print(items_not_performing[['ITEM_NAME', 'YoY_Growth_Rate']].head())

# # Identify the factors contributing to sales change
# data['Sales_Change'] = data['Yesterday_Sales_ThisYear'] - data['Yesterday_Sales_LastYear']

# # Factors Contributing to Sales Change
# print("\nFactors Contributing to Sales Change:")
# print(data[['ITEM_NAME', 'VENDOR_NAME', 'SUBCATEGORY', 'Sales_Change']].sort_values(by='Sales_Change', ascending=False).head())
