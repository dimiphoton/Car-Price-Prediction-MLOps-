# model_tracking.py
import mlflow
from mlflow.tracking import MlflowClient
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import os

# Define constants
EXPERIMENT_NAME = "House Price Prediction"
MODEL_NAME = "RandomForestRegressor"

# Load and preprocess data
def load_data():
    # Load data (replace with actual data loading code)
    data = pd.read_csv('data/house_prices.csv')
    # Perform preprocessing steps (replace with actual preprocessing code)
    # For example, handle missing values, encode categorical variables, etc.
    return data

# Train and evaluate model
def train_evaluate_model(data):
    X = data.drop(['SalePrice'], axis=1)
    y = data['SalePrice']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    mae = mean_absolute_error(y_test, y_pred)

    return model, rmse, mae

# Log metrics and artifacts
def log_metrics_and_artifacts(model, rmse, mae):
    mlflow.log_metric("RMSE", rmse)
    mlflow.log_metric("MAE", mae)

    # Log model artifact
    mlflow.sklearn.log_model(model, "model")

# Main function to run experiment
def run_experiment():
    # Start MLFlow run
    with mlflow.start_run(run_name="House Price Prediction Run") as run:
        # Load data
        data = load_data()

        # Train and evaluate model
        model, rmse, mae = train_evaluate_model(data)

        # Log metrics and model artifact
        log_metrics_and_artifacts(model, rmse, mae)

        # Register model
        client = MlflowClient()
        client.create_registered_model(name=MODEL_NAME, tags={"version": "1"})

        # Log experiment information
        mlflow.set_experiment(EXPERIMENT_NAME)
        experiment_id = mlflow.get_experiment_by_name(EXPERIMENT_NAME).experiment_id
        mlflow.set_tag("experiment_id", experiment_id)

if __name__ == "__main__":
    mlflow.set_tracking_uri("http://mlflow:5000")
    run_experiment()
