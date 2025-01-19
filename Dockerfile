FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements/ requirements/
RUN pip install --no-cache-dir -r requirements/prod.txt

# Copy application
COPY . .

# Make entrypoint script executable
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]