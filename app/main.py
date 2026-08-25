from fastapi import FastAPI
from app import models
from app.database import engine

app= FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/info")
async def info():
    return {"name": "StockFlow", 
            "version": "1.0.0",
            "description": "Warehouse management API"}
