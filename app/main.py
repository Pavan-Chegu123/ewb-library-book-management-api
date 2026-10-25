"""Application entry point."""
from fastapi import FastAPI
from . import models
from .database import Base, engine
from .routes import router as books_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="EWB Library Book Management API",
    description="A beginner-friendly CRUD API built with FastAPI, SQLAlchemy, and SQLite.",
    version="1.0.0",
)
app.include_router(books_router)


@app.get("/", tags=["General"])
def home():
    return {
        "message": "Welcome to the EWB Library Book Management API",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", tags=["General"])
def health():
    return {"status": "ok"}
