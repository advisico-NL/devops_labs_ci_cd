from fastapi import FastAPI

app = FastAPI(
    title="Pi5 DevOps Lab",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "application": "Pi5 DevOps Lab",
        "version": "0.1.0",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/version")
def version():
    return {
        "application": "Pi5 DevOps Lab",
        "version": "0.1.2"
    }
