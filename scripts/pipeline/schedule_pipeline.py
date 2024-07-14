# schedule_pipeline.py
from prefect.deployments import Deployment
from prefect.infrastructure.docker import DockerContainer
from training_pipeline import training_pipeline

# Define Docker container infrastructure
docker_block = DockerContainer(image="your_docker_image:latest")

# Define deployment
deployment = Deployment.build_from_flow(
    flow=training_pipeline,
    name="house_price_training",
    infrastructure=docker_block,
    parameters={
        "file_path": "data/house_prices_processed.csv",
        "target_column": "SalePrice"
    },
)

if __name__ == "__main__":
    deployment.apply()
