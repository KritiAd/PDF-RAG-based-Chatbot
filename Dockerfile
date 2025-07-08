# Use official lightweight Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy your entire project into the container
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    CHROMA_ANONYMIZED_TELEMETRY=False \
    NLTK_DATA=/app/nltk_data

# Install dependencies
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && python -m nltk.downloader stopwords

# Expose the FastAPI port
EXPOSE 8000

# Start your FastAPI app from app.py
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "443", "--ssl-keyfile=cert.key", "--ssl-certfile=cert.pem"]

