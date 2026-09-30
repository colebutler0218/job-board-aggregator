from fastapi import FastAPI

app = FastAPI(title="Job Board Aggregator")

@app.get("/health")
def health():
        return {"status" : "ok"}