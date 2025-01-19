# Remove the old file
rm entrypoint.sh

# Create new file with proper line endings
cat > entrypoint.sh << 'EOF'
#!/bin/sh

# Function to wait for postgres
wait_for_postgres() {
    echo "Waiting for PostgreSQL..."
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
        sleep 0.1
    done
    echo "PostgreSQL started"
}

# Wait for PostgreSQL
wait_for_postgres

# Run migrations using alembic
echo "Running database migrations..."
alembic upgrade head

# Start the FastAPI application
echo "Starting FastAPI application..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
EOF