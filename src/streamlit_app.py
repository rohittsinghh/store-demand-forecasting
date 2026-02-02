import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Store Demand Dashboard", layout="wide")

st.title("📊 Store Demand Forecasting Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv("data/raw/train.csv", parse_dates=["date"])
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
store = st.sidebar.selectbox("Select Store", df["store"].unique())
item = st.sidebar.selectbox("Select Item", df["item"].unique())

filtered = df[(df.store == store) & (df.item == item)]

# KPI Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Avg Sales", round(filtered.sales.mean(), 2))
col2.metric("Max Sales", filtered.sales.max())
col3.metric("Min Sales", filtered.sales.min())

# Sales Trend
st.subheader("Sales Trend Over Time")
fig, ax = plt.subplots(figsize=(10,4))
ax.plot(filtered.date, filtered.sales)
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
st.pyplot(fig)

# Weekend vs Weekday
st.subheader("Weekend vs Weekday Demand")
filtered["day_type"] = filtered.date.dt.dayofweek >= 5
filtered.groupby("day_type")["sales"].mean().plot(kind="bar", ax=ax)
st.pyplot(fig)
