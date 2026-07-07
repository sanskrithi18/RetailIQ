import pandas as pd

data = {
    "Date": ["2025-07-07"] * 5,
    "Brand": ["Samsung", "Apple", "Vivo", "Redmi", "Samsung"],
    "Model": ["A36", "iPhone 15", "T4", "Note 14", "S24"],
    "Quantity": [2, 1, 3, 2, 1],
    "Cost Price": [18000, 65000, 15000, 14000, 52000],
    "Selling Price": [21000, 72000, 17500, 16800, 59000],
    "Stock": [8, 5, 4, 2, 3]
}

df = pd.DataFrame(data)
df.to_excel("data/sales.xlsx", index=False)

print("sales.xlsx created successfully!")