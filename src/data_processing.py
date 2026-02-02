import pandas as pd

def load_data(path):
    df = pd.read_csv(path, parse_dates=["date"])
    return df

def basic_cleaning(df):
    df = df.sort_values("date")
    df = df.reset_index(drop=True)
    return df
