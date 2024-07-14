# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables for MLFlow
ENV MLFLOW_TRACKING_URI http://mlflow:5000

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
