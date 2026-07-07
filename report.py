import pandas as pd

def save_report(summary):

    report = pd.DataFrame({
        "Metric": summary.keys(),
        "Value": summary.values()
    })

    report.to_excel("reports/summary.xlsx", index=False)