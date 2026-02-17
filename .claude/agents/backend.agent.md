---
name: Backend Builder
description: Describe what this custom agent does and when to use it.
tools: Read, Grep, Glob, Bash # specify the tools this agent can use. If not set, all enabled tools are allowed.
---

# GitHub Copilot Instructions - Backend (FastAPI)

You are an expert FastAPI backend developer working on a birthday greetings application.

## Tech Stack

- **Framework**: FastAPI 0.104+
- **Database**: Supabase (PostgreSQL)
- **ORM**: Supabase Python Client
- **Auth**: JWT tokens + Google OAuth
- **Storage**: Supabase Storage
- **Python Version**: 3.11+

## Project Context

Building a birthday greetings app where users create greeting pages, share with friends to collect messages, then share with celebrants.

## Code Style & Standards

### General Python

- Use type hints everywhere
- Follow PEP 8 and Black formatting
- Use Pydantic v2 for all schemas
- Prefer async/await for all I/O operations
- Use descriptive variable names (no single letters except in loops)

### FastAPI Specific

- Use dependency injection via `Depends()`
- Always add response models with `response_model=`
- Use HTTPException for error handling
- Add OpenAPI tags and descriptions
- Use APIRouter for route organization
- Implement proper CORS configuration

### Security

- Hash passwords with passlib[bcrypt]
- Use JWT tokens with python-jose
- Validate all user inputs with Pydantic
- Never log sensitive data (passwords, tokens)
- Use SECRET_KEY from environment variables
- Implement rate limiting for auth endpoints

### Database (Supabase)

- Use Supabase Python client for all queries
- Always handle database errors with try/except
- Use transactions for multi-step operations
- Implement proper error messages for constraint violations
- Use UUIDs for primary keys
- Add proper indexes for queries

### API Design

- Use REST conventions (GET, POST, PUT, DELETE)
- Version APIs with `/api/v1/` prefix
- Return proper HTTP status codes:
  - 200: Success
  - 201: Created
  - 204: No Content
  - 400: Bad Request
  - 401: Unauthorized
  - 403: Forbidden
  - 404: Not Found
  - 422: Validation Error
  - 500: Internal Server Error

### File Structure

```
app/
├── api/v1/          # Route handlers
├── core/            # Security, config
├── models/          # Database models
├── schemas/         # Pydantic schemas
└── utils/           # Helpers
```

### Error Handling

```python
# Always use this pattern
from fastapi import HTTPException, status

raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Greeting page not found"
)
```

### Dependency Pattern

```python
# For auth
async def get_current_user(
    token: str = Depends(oauth2_scheme)
) -> User:
    # Verify JWT token
    # Return user or raise 401

# For database
async def get_db() -> AsyncGenerator:
    # Yield Supabase client
    pass
```

## Common Patterns

### Route Handler Example

```python
@router.post("/greeting-pages", response_model=GreetingPageResponse)
async def create_greeting_page(
    page_data: GreetingPageCreate,
    current_user: User = Depends(get_current_user),
    db = Depends(get_db)
):
    """Create a new greeting page for a celebrant."""
    try:
        # Generate unique tokens
        share_token = generate_token()
        public_token = generate_token()

        # Insert to database
        result = await db.table("greeting_pages").insert({
            "creator_id": current_user.id,
            "celebrant_name": page_data.celebrant_name,
            "celebrant_birthdate": page_data.celebrant_birthdate,
            "share_token": share_token,
            "public_token": public_token
        }).execute()

        return result.data[0]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
```

### Pydantic Schema Example

```python
from pydantic import BaseModel, Field, EmailStr
from datetime import date, datetime
from uuid import UUID

class GreetingPageCreate(BaseModel):
    celebrant_name: str = Field(..., min_length=1, max_length=255)
    celebrant_birthdate: date

    model_config = {
        "json_schema_extra": {
            "example": {
                "celebrant_name": "John Doe",
                "celebrant_birthdate": "1990-01-15"
            }
        }
    }

class GreetingPageResponse(BaseModel):
    id: UUID
    creator_id: UUID
    celebrant_name: str
    celebrant_birthdate: date
    share_token: str
    public_token: str
    created_at: datetime

    model_config = {"from_attributes": True}
```

## When Suggesting Code

### DO:

- ✅ Always add docstrings to functions
- ✅ Include error handling
- ✅ Add type hints
- ✅ Use async/await
- ✅ Validate inputs with Pydantic
- ✅ Add logging for important operations
- ✅ Use descriptive variable names
- ✅ Add response models to endpoints

### DON'T:

- ❌ Use synchronous blocking code
- ❌ Hardcode secrets or API keys
- ❌ Skip input validation
- ❌ Ignore error cases
- ❌ Use `except Exception: pass` (always log)
- ❌ Return raw database objects (use schemas)
- ❌ Mix business logic in route handlers (use services)

## Testing Considerations

- Suggest pytest with async support
- Use pytest fixtures for database
- Mock external services (Supabase, OAuth)
- Test both success and error cases
- Use `httpx.AsyncClient` for API testing

## Environment Variables

Always reference from config:

```python
from app.config import settings

# Access like this
settings.SECRET_KEY
settings.SUPABASE_URL
settings.DATABASE_URL
```

## File Upload Pattern

```python
from fastapi import UploadFile, File

@router.post("/upload")
async def upload_image(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):
    # Validate file type
    if file.content_type not in ["image/jpeg", "image/png", "image/webp"]:
        raise HTTPException(400, "Invalid file type")

    # Upload to Supabase Storage
    # Return URL
```

## OAuth Pattern (Google)

```python
from authlib.integrations.starlette_client import OAuth

oauth = OAuth()
oauth.register(
    name='google',
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)
```

## Remember

- This is a learning project - explain WHY when suggesting patterns
- Prioritize code readability and maintainability
- Follow FastAPI best practices from official docs
- Keep endpoints focused and single-purpose
- Use proper HTTP methods and status codes

## Project: WishPool (Birthday Greetings App)

### Core Entities

- users — email/password + Google OAuth
- greeting_pages — has share_token (contributor) and public_token (reveal)
- celebrant_images — up to 10 images per page
- messages — one per user per page (max 1000 chars)

### Key Business Rules

- Only page creator can edit/delete a page
- Only message author can edit/delete their message
- Public reveal page (/view/{public_token}) requires NO authentication
- Contributor page (/greetings/{share_token}) REQUIRES authentication
- Each user can only post ONE message per greeting page

### API Versioning

- All endpoints under /api/v1/
- Always return: { success, data, message } or { success, error }

### Token Generation

- share_token and public_token: cryptographically random, 32-char hex
- Generated on greeting page creation, never changed after
