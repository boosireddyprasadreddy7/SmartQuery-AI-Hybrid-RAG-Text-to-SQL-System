from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hybrid AI Query System Running"}