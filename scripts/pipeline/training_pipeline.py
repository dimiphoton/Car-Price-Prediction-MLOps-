# training_pipeline.py
import pandas as pd
from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import os

# Load Dataset
@task(retries=3, cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def load_dataset(file_path):
    data = pd.read_csv(file_path)
    return data

# Preprocessing Steps
@task
def handle_missing_values(data):
    for column in data.select_dtypes(include=['float64', 'int64']).columns:
        data[column].fillna(data[column].median(), inplace=True)
    for column in data.select_dtypes(include=['object']).columns:
        data[column].fillna(data[column].mode()[0], inplace=True)
    return data

@task
def encode_categorical(data):
    data = pd.get_dummies(data, drop_first=True)
    return data

@task
def scale_numerical(data):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
    data[numerical_cols] = scaler.fit_transform(data[numerical_cols])
    return data

# Split Dataset
@task
def split_dataset(data, target_column, test_size=0.2, random_state=42):
    from sklearn.model_selection import train_test_split
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

# Train Models
@task
def train_and_evaluate(X_train, X_test, y_train, y_test):
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(random_state=42),
        "Gradient Boosting": GradientBoostingRegressor(random_state=42)
    }
    
    mlflow.set_experiment("house-price-prediction")
    
    best_model = None
    best_rmse = float('inf')
    
    for model_name, model in models.items():
        with mlflow.start_run(run_name=model_name):
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            rmse = mean_squared_error(y_test, y_pred, squared=False)
            mae = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            mlflow.log_param("model", model_name)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)
            mlflow.sklearn.log_model(model, model_name)
            
            if rmse < best_rmse:
                best_rmse = rmse
                best_model = model

    return best_model

@flow
def training_pipeline(file_path, target_column):
    data = load_dataset(file_path)
    data = handle_missing_values(data)
    data = encode_categorical(data)
    data = scale_numerical(data)
    X_train, X_test, y_train, y_test = split_dataset(data, target_column).result()
    best_model = train_and_evaluate(X_train, X_test, y_train, y_test)
    print("Training pipeline completed.")

if __name__ == "__main__":
    file_path = 'data/house_prices_processed.csv'  # Update with your dataset path
    target_column = 'SalePrice'
    training_pipeline(file_path, target_column)
