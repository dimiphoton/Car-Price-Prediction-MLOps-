# deploy_model.py
import mlflow.pyfunc
from mlflow.models.signature import infer_signature

def deploy_model(model_uri):
    # Load the model
    model = mlflow.pyfunc.load_model(model_uri)

    # Example: Deploying to AWS Lambda (replace with actual deployment logic)
    # Example assumes using mlflow.pyfunc.load_model for loading the model
    # You may need additional steps depending on your deployment target
    # For AWS Lambda, you typically package your model into a Docker container or zip file
    
    # Example code snippet for AWS Lambda deployment
    import boto3
    client = boto3.client('lambda')

    response = client.create_function(
        FunctionName='my-model-function',
        Runtime='python3.8',
        Role='arn:aws:iam::123456789012:role/lambda-role',
        Handler='predict.lambda_handler',
        Code={
            'S3Bucket': 'my-bucket',
            'S3Key': 'model.zip'
        }
    )

    print(response)

if __name__ == "__main__":
    model_uri = "models:/House Price Prediction/Production"
    deploy_model(model_uri)
