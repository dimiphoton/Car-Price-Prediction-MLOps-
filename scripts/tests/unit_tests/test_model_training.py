# tests/test_model_training.py
import pytest
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from train_models import train_and_evaluate

@pytest.fixture
def sample_data():
    data = {
        "num_col": [1, 2, 3, 4],
        "cat_col_a": [1, 0, 1, 0],
        "target": [100, 200, 150, 300]
    }
    return pd.DataFrame(data)

def test_train_and_evaluate(sample_data):
    X = sample_data.drop("target", axis=1)
    y = sample_data["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    rmse, mae, r2 = train_and_evaluate(model, X_train, X_test, y_train, y_test)
    assert rmse >= 0
    assert mae >= 0
    assert -1 <= r2 <= 1
