# select_best_model.py
import mlflow
import mlflow.sklearn

def select_best_model(experiment_name):
    client = mlflow.tracking.MlflowClient()
    experiment = client.get_experiment_by_name(experiment_name)
    runs = client.search_runs(experiment.experiment_id, order_by=["metrics.rmse ASC"])
    best_run = runs[0]
    best_model_uri = best_run.info.artifact_uri + '/' + best_run.data.params['model']
    best_model = mlflow.sklearn.load_model(best_model_uri)
    return best_model, best_run

if __name__ == "__main__":
    experiment_name = "house-price-prediction"
    best_model, best_run = select_best_model(experiment_name)
    print(f"Best Model: {best_run.data.params['model']}")
    print(f"RMSE: {best_run.data.metrics['rmse']}")
    print(f"MAE: {best_run.data.metrics['mae']}")
    print(f"R2: {best_run.data.metrics['r2']}")
