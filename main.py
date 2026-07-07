from analyzer import analyze_sales
from report import save_report
from charts import revenue_chart
from database import save_database

df, summary = analyze_sales("data/sales.xlsx")

print("RetailIQ Dashboard")
print("-"*40)

for k,v in summary.items():
    print(k,":",v)

save_report(summary)

revenue_chart(df)

save_database(df)

print("\nDone!")