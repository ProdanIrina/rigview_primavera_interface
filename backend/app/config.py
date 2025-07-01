import os
from dotenv import load_dotenv

load_dotenv()
DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")
JWT_SECRET = os.getenv("JWT_SECRET", "superjwtsecretkey")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
