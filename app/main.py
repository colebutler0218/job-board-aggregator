from fastapi import FastAPI
from app import config

from app import models  # noqa: F401  (importing registers the tables on Base)
from app.db import Base, engine

Base.metadata.create_all(engine)

app = FastAPI(title="Job Board Aggregator")

@app.get("/health")
def health():
    return {"status" : "ok"}
