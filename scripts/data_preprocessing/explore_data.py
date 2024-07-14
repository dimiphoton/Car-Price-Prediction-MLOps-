# explore_data.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def explore_data(data):
    print("Data Info:")
    print(data.info())
    print("\nSummary Statistics:")
    print(data.describe())

    # Plotting
    plt.figure(figsize=(10, 6))
    sns.histplot(data['SalePrice'], kde=True)
    plt.title('Distribution of Sale Prices')
    plt.show()

if __name__ == "__main__":
    file_path = 'data/house_prices.csv'  # Update with your dataset path
    data = pd.read_csv(file_path)
    explore_data(data)
