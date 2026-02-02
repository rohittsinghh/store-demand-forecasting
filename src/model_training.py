import lightgbm as lgb
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error
import joblib

def train_model(df):
    df = df.dropna()

    features = [c for c in df.columns if c not in ["date","sales"]]
    X = df[features]
    y = df["sales"]

    model = lgb.LGBMRegressor(
        n_estimators=1000,
        learning_rate=0.05,
        max_depth=8
    )

    model.fit(X, y)

    joblib.dump(model, "models/lgb_model.pkl")
    return model
