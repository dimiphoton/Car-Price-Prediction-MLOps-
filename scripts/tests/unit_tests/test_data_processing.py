# tests/test_data_processing.py
import pytest
import pandas as pd
from handle_missing_values import handle_missing_values
from encode_categorical import encode_categorical
from scale_numerical import scale_numerical

@pytest.fixture
def sample_data():
    data = {
        "num_col": [1, 2, None, 4],
        "cat_col": ["a", "b", None, "a"],
        "target": [100, 200, 150, 300]
    }
    return pd.DataFrame(data)

def test_handle_missing_values(sample_data):
    processed_data = handle_missing_values(sample_data)
    assert processed_data.isnull().sum().sum() == 0

def test_encode_categorical(sample_data):
    sample_data = handle_missing_values(sample_data)
    processed_data = encode_categorical(sample_data)
    assert "cat_col_a" in processed_data.columns

def test_scale_numerical(sample_data):
    sample_data = handle_missing_values(sample_data)
    sample_data = encode_categorical(sample_data)
    processed_data = scale_numerical(sample_data)
    assert processed_data["num_col"].mean() == pytest.approx(0, abs=1e-1)
