from src.data_processing import load_data, basic_cleaning
from src.feature_engineering import create_features
from src.model_training import train_model

df = load_data("data/raw/train.csv")
df = basic_cleaning(df)
df = create_features(df)

model = train_model(df)
print("✅ Model trained successfully")
