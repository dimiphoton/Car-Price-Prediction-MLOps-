# encode_categorical.py
import pandas as pd

def encode_categorical(data):
    data = pd.get_dummies(data, drop_first=True)
    return data

if __name__ == "__main__":
    file_path = 'data/house_prices.csv'  # Update with your dataset path
    data = pd.read_csv(file_path)
    data = encode_categorical(data)
    print(data.head())
