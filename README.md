# Store Demand Forecasting 📊

## Overview
This project focuses on forecasting retail store demand using historical sales data.
It applies time-series analysis, feature engineering, and machine learning to support
business decision-making.

## Key Features
- Data cleaning and preprocessing (structured data)
- Advanced feature engineering (lags, rolling stats, EWMA)
- Trend and seasonality analysis
- Sales dashboards and visualizations
- Machine learning forecasting using LightGBM
- Linux-based reproducible pipeline

## Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- LightGBM
- Scikit-learn
- Linux

## Project Structure

store-demand-forecasting/
├── data/
├── notebooks/
├── src/
├── reports/
├── models/
├── run_pipeline.py
├── requirements.txt

## How to Run
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run_pipeline.py
```
## Dashboard
An interactive Streamlit dashboard allows users to:
- Filter sales by store and item
- View KPIs and trends
- Analyze weekday vs weekend demand

Run:
```bash
streamlit run src/streamlit_app.py
---
```bash

