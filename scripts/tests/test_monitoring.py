# tests/test_monitoring.py
import pytest
import pandas as pd
from monitoring import generate_dashboard
from set_up_alerts import check_model_drift

@pytest.fixture
def sample_data():
    data = {
        "SalePrice": [200000, 250000, 300000, 350000]
    }
    return pd.DataFrame(data)

def test_generate_dashboard(sample_data, tmpdir):
    reference_data = sample_data.copy()
    current_data = sample_data.copy()
    output_file = tmpdir.join("dashboard.html")
    generate_dashboard(reference_data, current_data, str(output_file))
    assert output_file.exists()

def test_check_model_drift(sample_data):
    reference_data = sample_data.copy()
    current_data = sample_data.copy()
    suite = check_model_drift(reference_data, current_data)
    assert suite.as_dict()['tests'][0]['status'] == 'PASS'
