import time
import psycopg2
import os


def wait_for_db():
    host = os.getenv("POSTGRES_HOST", "db")
    port = os.getenv("POSTGRES_PORT", "5432")
    database = os.getenv("POSTGRES_DB", "microservice_db")
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")

    max_retries = 30
    retries = 0

    while retries < max_retries:
        try:
            conn = psycopg2.connect(
                dbname=database,
                user=user,
                password=password,
                host=host,
                port=port
            )
            conn.close()
            print("Database is ready!")
            return True
        except psycopg2.OperationalError:
            retries += 1
            print(f"Waiting for database... {retries}/{max_retries}")
            time.sleep(1)

    raise Exception("Could not connect to database")


if __name__ == "__main__":
    wait_for_db()