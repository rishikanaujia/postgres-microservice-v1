FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements/ requirements/
RUN pip install --no-cache-dir -r requirements/prod.txt

# Create db_check script
RUN mkdir -p scripts
RUN echo 'import time\nimport psycopg2\nimport os\n\ndef wait_for_db():\n    host = os.getenv("POSTGRES_HOST", "db")\n    port = os.getenv("POSTGRES_PORT", "5432")\n    database = os.getenv("POSTGRES_DB", "microservice_db")\n    user = os.getenv("POSTGRES_USER", "postgres")\n    password = os.getenv("POSTGRES_PASSWORD", "postgres")\n    \n    max_retries = 30\n    retries = 0\n    \n    while retries < max_retries:\n        try:\n            conn = psycopg2.connect(\n                dbname=database,\n                user=user,\n                password=password,\n                host=host,\n                port=port\n            )\n            conn.close()\n            print("Database is ready!")\n            return True\n        except psycopg2.OperationalError:\n            retries += 1\n            print(f"Waiting for database... {retries}/{max_retries}")\n            time.sleep(1)\n    \n    raise Exception("Could not connect to database")\n\nif __name__ == "__main__":\n    wait_for_db()' > scripts/db_check.py

# Copy application
COPY . .

# Create startup script
RUN echo '#!/bin/bash\npython /app/scripts/db_check.py && uvicorn app.main:app --host 0.0.0.0 --port 8000' > /entrypoint.sh && \
    chmod +x /entrypoint.sh

CMD ["/bin/bash", "/entrypoint.sh"]