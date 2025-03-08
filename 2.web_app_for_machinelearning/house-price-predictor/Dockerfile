# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app and the model into the container
COPY app.py .
COPY house_price_model.pkl .

# Expose the Streamlit port
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# Build the Docker image
#docker build -t house-price-predictor .

# Run the Docker container
#docker run  -d -p 8502:8501 house-price-predictor
