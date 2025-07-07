from jose import jwt
from .config import JWT_SECRET, JWT_ALGORITHM
from datetime import datetime, timedelta

def create_jwt_token(username):
    token_payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=12)
    }
    return jwt.encode(token_payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
