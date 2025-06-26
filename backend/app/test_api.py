from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"msg": "merge"}

@app.get("/ping")
def ping():
    return {"pong": True}
