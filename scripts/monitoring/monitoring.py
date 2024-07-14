# monitoring.py
import pandas as pd
from whylogs import DatasetProfile, get_or_create_session

def monitor_model_performance(data):
    session = get_or_create_session()
    profile = DatasetProfile("model_performance")
    profile.track_dataframe(data)
    session.log(profile)
    session.close()

if __name__ == "__main__":
    data = pd.read_csv('data/monitoring_data.csv')
    monitor_model_performance(data)
