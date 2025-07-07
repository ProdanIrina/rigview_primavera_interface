import pyodbc
from . import DB_CONNECTION_STRING

def get_db_conn():
    return pyodbc.connect(DB_CONNECTION_STRING)
