"""Pydantic schemas for greeting page creation and responses."""

from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, Field


class GreetingCreateRequest(BaseModel):
    """Request payload for creating a greeting page."""

    celebrant_full_name: str = Field(..., min_length=1, max_length=255)
    celebrant_birthdate: date
    cover_photo_url: str | None = Field(default=None, max_length=2048)
    gallery_image_urls: list[str] = Field(default_factory=list, max_length=10)


class GreetingCreateResponse(BaseModel):
    """Response payload returned after creating a greeting page."""

    id: UUID
    celebrant_full_name: str
    celebrant_birthdate: date
    cover_photo_url: str | None
    gallery_image_urls: list[str]
    share_token: str
    public_token: str
    contributor_link: str
    reveal_link: str
    created_at: datetime

    model_config = {"from_attributes": True}
