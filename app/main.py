from fastapi import FastAPI
from app import config

app = FastAPI(title="Job Board Aggregator")

@app.get("/health")
def health():
    return {"status" : "ok"}
