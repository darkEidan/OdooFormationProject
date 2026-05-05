import psycopg
from psycopg.rows import dict_row


def get_connection():
    return psycopg.connect(
        dbname="OdooFormationProject",
        user="postgres",
        password="test123",
        host="localhost",
        port="5432",
        row_factory=dict_row
    )

