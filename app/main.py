from fastapi import FastAPI

app= FastAPI()

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
