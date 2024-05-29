from fastapi import FastAPI
from app.api.endpoints import recommendations
import app.snowflakes.database as db

app = FastAPI()

app.include_router(recommendations.router, prefix="/api/v1", tags=["recommendations"])

@app.on_event("startup")
def startup_event():
    db.create_connection()

@app.on_event("shutdown")
def shutdown_event():
    db.close_connection()
