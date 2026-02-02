# src/dashboard.py
import matplotlib.pyplot as plt

def plot_sales(df):
    daily = df.groupby("date")["sales"].sum()
    daily.plot(figsize=(12,5))
    plt.title("Total Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.show()
