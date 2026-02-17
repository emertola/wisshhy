"""Greeting endpoints (Step 1: create greeting page)."""

from fastapi import APIRouter, status

from app.schemas.greeting import GreetingCreateRequest, GreetingCreateResponse
from app.services.greeting_service import greeting_service

router = APIRouter(prefix="/greetings", tags=["Greetings"])


@router.post(
    "",
    response_model=GreetingCreateResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create greeting page",
    description="Create a greeting page and return contributor and reveal links.",
)
def create_greeting(payload: GreetingCreateRequest) -> GreetingCreateResponse:
    """Create a new greeting page."""
    return greeting_service.create_greeting(payload)
