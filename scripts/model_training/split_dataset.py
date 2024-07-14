# split_data.py
import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataset(data, target_column, test_size=0.2, random_state=42):
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    file_path = 'data/house_prices_processed.csv'  # Update with your preprocessed dataset path
    data = pd.read_csv(file_path)
    target_column = 'SalePrice'
    X_train, X_test, y_train, y_test = split_dataset(data, target_column)
    print("Train set size:", X_train.shape)
    print("Test set size:", X_test.shape)
