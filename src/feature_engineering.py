import pandas as pd

def create_features(df):
    df["year"] = df.date.dt.year
    df["month"] = df.date.dt.month
    df["day"] = df.date.dt.day
    df["dayofweek"] = df.date.dt.dayofweek
    df["weekofyear"] = df.date.dt.isocalendar().week
    df["is_weekend"] = df.dayofweek >= 5

    for lag in [7, 14, 28]:
        df[f"lag_{lag}"] = df.groupby(["store","item"])["sales"].shift(lag)

    df["rolling_mean_28"] = (
        df.groupby(["store","item"])["sales"]
        .shift(1)
        .rolling(28)
        .mean()
    )

    df["ewma_14"] = (
        df.groupby(["store","item"])["sales"]
        .shift(1)
        .ewm(span=14)
        .mean()
    )

    return df
