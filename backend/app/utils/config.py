import os
from dotenv import load_dotenv

load_dotenv()

DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")

JWT_SECRET = os.getenv("JWT_SECRET", "superjwtsecretkey")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

PRIMAVERA_API_URL = os.getenv("PRIMAVERA_API_URL")
PRIMAVERA_USER = os.getenv("PRIMAVERA_USER")
PRIMAVERA_PASS = os.getenv("PRIMAVERA_PASS")