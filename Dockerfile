# Use official Python 3.12.7 image as base
FROM python:3.12.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the files from your local machine into the container
COPY . .

# Expose port 8080 for FastAPI
EXPOSE 8080

# Set environment variables (if needed)
# COPY .env .env  # Uncomment if you want to copy your .env file into the container

# Run the FastAPI app using Uvicorn, set host to 0.0.0.0 to make it accessible from outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
