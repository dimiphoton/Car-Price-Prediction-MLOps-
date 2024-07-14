# handle_missing_values.py
import pandas as pd

def handle_missing_values(data):
    # Example: Fill missing values with the median for numerical columns
    for column in data.select_dtypes(include=['float64', 'int64']).columns:
        data[column].fillna(data[column].median(), inplace=True)
    
    # Example: Fill missing values with the mode for categorical columns
    for column in data.select_dtypes(include=['object']).columns:
        data[column].fillna(data[column].mode()[0], inplace=True)
    
    return data

if __name__ == "__main__":
    file_path = 'data/house_prices.csv'  # Update with your dataset path
    data = pd.read_csv(file_path)
    data = handle_missing_values(data)
    print(data.isnull().sum())
