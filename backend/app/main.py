"""Bare minimum FastAPI application."""
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from supabase import Client

from app.database import get_db

app = FastAPI(title="Wisshhy API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Wisshhy API is running"}


@app.get("/health")
async def health(db: Client = Depends(get_db)):
    """Health check with database connection test."""
    try:
        # Test database connection
        # This is a simple ping - adjust based on your tables
        db.table("_migrations").select("*").limit(1).execute()
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "healthy",
            "database": "disconnected",
            "error": str(e)
        }
