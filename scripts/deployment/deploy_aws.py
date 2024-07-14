#!/bin/bash

# Variables
APP_NAME="house-price-prediction"
DOCKER_IMAGE="your_docker_image:latest"
AWS_REGION="us-west-2"

# Build Docker image
docker build -t $DOCKER_IMAGE .

# Authenticate Docker to ECR
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin <your_ecr_repository>

# Tag and push Docker image to ECR
docker tag $DOCKER_IMAGE <your_ecr_repository>/$DOCKER_IMAGE
docker push <your_ecr_repository>/$DOCKER_IMAGE

# Deploy on AWS Elastic Beanstalk
eb init -p docker $APP_NAME --region $AWS_REGION
eb create $APP_NAME-env
eb deploy
