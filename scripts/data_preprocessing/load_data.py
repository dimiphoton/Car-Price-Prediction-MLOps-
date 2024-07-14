# load_data.py
import pandas as pd

def load_dataset(file_path):
    data = pd.read_csv(file_path)
    return data

if __name__ == "__main__":
    file_path = 'data/raw/train.csv' 
    data = load_dataset(file_path)
    print(data.head())
