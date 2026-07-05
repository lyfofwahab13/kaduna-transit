import os
import json
import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.environ.get("DATABASE_URL")


def get_conn():
    return psycopg2.connect(DATABASE_URL)


def init_db():
    """Create routes table if it doesn't exist and import routes.json if table is empty."""
    conn = get_conn()
    cur  = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS routes (
            id SERIAL PRIMARY KEY,
            origin TEXT NOT NULL,
            destination TEXT NOT NULL,
            vehicle TEXT NOT NULL,
            fare TEXT NOT NULL,
            duration TEXT NOT NULL,
            notes TEXT NOT NULL
        )
