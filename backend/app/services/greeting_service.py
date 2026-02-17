"""Service layer for greeting page creation."""

from datetime import datetime, timezone
from secrets import token_hex
from typing import Dict
from uuid import UUID, uuid4

from app.schemas.greeting import GreetingCreateRequest, GreetingCreateResponse


class GreetingService:
    """In-memory greeting service for initial feature delivery."""

    def __init__(self) -> None:
        self._greetings: Dict[UUID, GreetingCreateResponse] = {}

    def create_greeting(self, payload: GreetingCreateRequest) -> GreetingCreateResponse:
        """Create a greeting page with contributor and reveal tokens."""
        greeting_id = uuid4()
        share_token = token_hex(16)
        public_token = token_hex(16)
        created_at = datetime.now(timezone.utc)

        greeting = GreetingCreateResponse(
            id=greeting_id,
            celebrant_full_name=payload.celebrant_full_name,
            celebrant_birthdate=payload.celebrant_birthdate,
            cover_photo_url=payload.cover_photo_url,
            gallery_image_urls=payload.gallery_image_urls,
            share_token=share_token,
            public_token=public_token,
            contributor_link=f"/greetings/{share_token}",
            reveal_link=f"/view/{public_token}",
            created_at=created_at,
        )

        self._greetings[greeting_id] = greeting
        return greeting


greeting_service = GreetingService()
