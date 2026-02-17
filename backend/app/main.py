"""Bare minimum FastAPI application."""
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import Client

from app.api.v1.greetings import router as greetings_router
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

app.include_router(greetings_router, prefix="/api/v1")


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "Wisshhy API is running"}


@app.get("/health")
async def health(db: Client = Depends(get_db)) -> dict[str, str]:
    """Health check with database connection test."""
    try:
        # Test database connection
        db.table("_migrations").select("*").limit(1).execute()
        return {"status": "healthy", "database": "connected"}
    except Exception as error:
        return {
            "status": "healthy",
            "database": "disconnected",
            "error": str(error),
        }
