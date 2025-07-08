import pyodbc
from app.utils.config import DB_CONNECTION_STRING

def get_db_conn():
    return pyodbc.connect(DB_CONNECTION_STRING)
