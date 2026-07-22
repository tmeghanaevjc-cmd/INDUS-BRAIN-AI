from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "INDUS BRAIN AI",
        "status": "Prototype",
        "hackathon": "ET AI Hackathon 2026"
    }
