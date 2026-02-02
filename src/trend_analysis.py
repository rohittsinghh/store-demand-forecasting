# src/trend_analysis.py
def monthly_trend(df):
    return df.groupby(["year","month"])["sales"].mean()
