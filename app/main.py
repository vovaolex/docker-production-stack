import os
import psycopg2
from fastapi import FastAPI

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppassword")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


@app.get("/")
def root():
    return {"message": "Docker production stack is running"}


@app.get("/health")
def health():
    try:
        conn = get_connection()
        conn.close()

        return {
            "status": "ok",
            "database": "connected"
        }

    except Exception as e:
        return {
            "status": "error",
            "database": str(e)
        }