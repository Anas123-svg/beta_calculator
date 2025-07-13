from fastapi import FastAPI
from app.api.routes import router
from app.config.cors import add_cors_middleware

app = FastAPI(title="Stock Market Analysis")
app = FastAPI()
add_cors_middleware(app)

app.include_router(router, prefix="/api/v1/stocks", tags=["Stocks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Stock Market Analysis API!"}