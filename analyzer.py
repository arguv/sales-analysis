import pandas as pd
from helpers import calculate_total, format_currency
import os
import json

# Read data
df = pd.read_csv('data/sales.csv')

# Calculate total for each row
totals = []
for index, row in df.iterrows():
    total = calculate_total(row['quantity'], row['price'])
    totals.append(total)

# Add totals to our data
df['total'] = totals

# Display with formatted totals
print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

# Show grand total
grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")

# Calculate the report once so every export contains the same results.
summary = pd.DataFrame([{
    'sales_count': len(df),
    'units_sold': df['quantity'].sum(),
    'grand_total': grand_total,
}])
product_report = (
    df.groupby('product', as_index=False, dropna=False)
    .agg(units_sold=('quantity', 'sum'), total_sales=('total', 'sum'))
)

# -----------------------------------------------

# Create output directory
os.makedirs('output', exist_ok=True)

# Save as different formats
# 1. JSON format (good for web APIs)
report = {
    'sales': json.loads(df.to_json(orient='records')),
    'summary': json.loads(summary.to_json(orient='records'))[0],
    'by_product': json.loads(product_report.to_json(orient='records')),
}
with open('output/sales_data.json', 'w', encoding='utf-8') as report_file:
    json.dump(report, report_file, indent=2, ensure_ascii=False)

# 2. Excel format (good for sharing)
with pd.ExcelWriter('output/sales_data.xlsx') as writer:
    summary.to_excel(writer, sheet_name='Summary', index=False)
    product_report.to_excel(writer, sheet_name='By Product', index=False)
    df.to_excel(writer, sheet_name='Sales', index=False)

# 3. Updated CSV (with our new total column)
df.to_csv('output/sales_with_totals.csv', index=False)
summary.to_csv('output/sales_summary.csv', index=False)
product_report.to_csv('output/sales_by_product.csv', index=False)

print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx")
print("- output/sales_with_totals.csv")
print("- output/sales_summary.csv")
print("- output/sales_by_product.csv")
