import os
import psycopg
from psycopg.rows import dict_row

def get_connection():
    return psycopg.connect(
        dbname=os.environ.get("DB_NAME", "OdooFormationProject"),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", ""),
        host=os.environ.get("DB_HOST", "localhost"),
        port=os.environ.get("DB_PORT", "5432"),
        row_factory=dict_row
    )