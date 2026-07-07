import pandas as pd

def analyze_sales(file_path):
    df = pd.read_excel(file_path)

    df["Revenue"] = df["Quantity"] * df["Selling Price"]
    df["Profit"] = (df["Selling Price"] - df["Cost Price"]) * df["Quantity"]

    summary = {
        "Total Revenue": df["Revenue"].sum(),
        "Total Profit": df["Profit"].sum(),
        "Top Brand": df.groupby("Brand")["Revenue"].sum().idxmax(),
        "Top Model": df.groupby("Model")["Revenue"].sum().idxmax(),
        "Low Stock": df[df["Stock"] < 5]["Model"].tolist()
    }

    return df, summary