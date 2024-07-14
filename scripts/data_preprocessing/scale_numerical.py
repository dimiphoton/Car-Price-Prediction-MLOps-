# scale_numerical.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

def scale_numerical(data):
    scaler = StandardScaler()
    numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
    data[numerical_cols] = scaler.fit_transform(data[numerical_cols])
    return data

if __name__ == "__main__":
    file_path = 'data/house_prices.csv'  # Update with your dataset path
    data = pd.read_csv(file_path)
    data = scale_numerical(data)
    print(data.head())
