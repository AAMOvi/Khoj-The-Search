from fastapi import FastAPI
from search_engine.load_data import load_dataset
from search_engine.search import KhojSearchEngine

app = FastAPI()

engine = KhojSearchEngine()


@app.get("/")
def home():
    return {"message": "Khoj Search API Running"}


@app.get("/search")
def search(q: str):
    results = engine.search(q)
    return {"query": q, "results": results}