# train_models.py
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def train_and_evaluate(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return rmse, mae, r2

if __name__ == "__main__":
    file_path = 'data/house_prices_processed.csv'  # Update with your preprocessed dataset path
    data = pd.read_csv(file_path)
    target_column = 'SalePrice'
    X_train, X_test, y_train, y_test = split_dataset(data, target_column)
    
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(random_state=42),
        "Gradient Boosting": GradientBoostingRegressor(random_state=42)
    }
    
    mlflow.set_experiment("house-price-prediction")
    
    for model_name, model in models.items():
        with mlflow.start_run(run_name=model_name):
            rmse, mae, r2 = train_and_evaluate(model, X_train, X_test, y_train, y_test)
            print(f"{model_name}: RMSE={rmse}, MAE={mae}, R2={r2}")
            mlflow.log_param("model", model_name)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)
            mlflow.sklearn.log_model(model, model_name)
