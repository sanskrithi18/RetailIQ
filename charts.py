import matplotlib.pyplot as plt

def revenue_chart(df):

    revenue = df.groupby("Brand")["Revenue"].sum()

    revenue.plot(kind="bar")

    plt.title("Revenue by Brand")

    plt.tight_layout()

    plt.savefig("charts/revenue.png")

    plt.close()