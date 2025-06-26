from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from cryptography.fernet import Fernet
from jose import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import pyodbc

# ================================
# Inițializări
# ================================

# Încarcă variabilele de mediu din fișierul .env
load_dotenv()

# Inițializează aplicația FastAPI
app = FastAPI()

# Permite accesul din frontend (React care rulează pe localhost:5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Citește cheia secretă și stringul de conexiune la baza de date din .env
SECRET_KEY = os.getenv("SECRET_KEY")
DB_CONN_STRING = os.getenv("DB_CONNECTION_STRING")
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
fernet = Fernet(SECRET_KEY.encode())  # Inițializează obiectul Fernet pentru criptare

# ================================
# MODELE DE DATE
# ================================

class Credentials(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str
    remember: bool

class Activity(BaseModel):
    activity_id: str
    name: str
    uwi: str
    start: str
    finish: str
    status: str
    rig_view_code: str
    gate: str

# ================================
# ENDPOINTURI
# ================================

@app.post("/login")
def login_user(data: LoginRequest):
    try:
        # === VALIDARE MOCK ===
        if data.username != "admin" or data.password != "test123":
            raise HTTPException(status_code=401, detail="Credentiale invalide")

        # === GENERARE JWT ===
        token_payload = {
            "sub": data.username,
            "exp": datetime.utcnow() + timedelta(hours=12)
        }
        token = jwt.encode(token_payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

        # === SALVARE CREDENTIAL DACA E NECESAR ===
        if data.remember:
            encrypted_user = fernet.encrypt(data.username.encode()).decode()
            encrypted_pass = fernet.encrypt(data.password.encode()).decode()
            conn = pyodbc.connect(DB_CONN_STRING)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO credentials (username, password, created_at)
                VALUES (?, ?, ?)
            """, (encrypted_user, encrypted_pass, datetime.utcnow()))
            conn.commit()

        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Endpoint pentru salvarea credentialelor criptate în baza de date
@app.post("/credentials")
def save_credentials(data: Credentials):
    try:
        encrypted_user = fernet.encrypt(data.username.encode()).decode()
        encrypted_pass = fernet.encrypt(data.password.encode()).decode()
        conn = pyodbc.connect(DB_CONN_STRING)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO credentials (username, password, created_at)
            VALUES (?, ?, ?)
        """, (encrypted_user, encrypted_pass, datetime.utcnow()))
        conn.commit()
        return {"message": "Credentiale salvate cu succes!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint pentru extragerea activităților filtrate care trebuie sincronizate
@app.get("/sync/activities")
def get_filtered_activities():
    # try:
    #     conn = pyodbc.connect(DB_CONN_STRING)
    #     cursor = conn.cursor()
    #     # Selectează doar activitățile care au codurile 'S' sau 'AR'
    #     cursor.execute("""
    #         SELECT activity_id, name, uwi, start_date, finish_date, status, rig_view_code, gate
    #         FROM activity_cache
    #         WHERE rig_view_code IN ('S', 'AR')
    #           AND uwi IS NOT NULL
    #           AND project_status NOT IN ('Completed', 'Canceled')
    #     """)
    #     rows = cursor.fetchall()
    #     result = []
    #     for row in rows:
    #         result.append({
    #             "activity_id": row[0],
    #             "name": row[1],
    #             "uwi": row[2],
    #             "start": str(row[3]),
    #             "finish": str(row[4]),
    #             "status": row[5],
    #             "rig_view_code": row[6],
    #             "gate": row[7]
    #         })
    #     return result
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))
    # mock de test
    return [
        {
            "activity_id": "ACT001",
            "name": "Drilling activity",
            "uwi": "UWI-123",
            "start": "2025-07-01",
            "finish": "2025-07-10",
            "status": "Not Started",
            "rig_view_code": "S",
            "gate": "G1"
        },
        {
            "activity_id": "ACT002",
            "name": "Flowline execution",
            "uwi": "UWI-124",
            "start": "2025-07-05",
            "finish": "2025-07-15",
            "status": "In Progress",
            "rig_view_code": "AR",
            "gate": "G2"
        }
    ]

# Endpoint pentru primirea alocărilor de riguri din RigView
@app.post("/update-rig")
def update_rig_allocation(data: dict):
    try:
        # Salvează payload-ul primit ca log în baza de date (tabelul sync_log)
        conn = pyodbc.connect(DB_CONN_STRING)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO sync_log (direction, payload, status, timestamp)
            VALUES (?, ?, ?, ?)
        """, ("R2P", str(data), "received", datetime.utcnow()))
        conn.commit()
        return {"message": "Rig received"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
