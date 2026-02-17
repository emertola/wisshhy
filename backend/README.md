# Wisshhy Backend - Minimal Setup

## Quick Start

1. **Create virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Run the server:**
   ```powershell
   uvicorn app.main:app --reload --port 8000
   ```

4. **Visit:** http://localhost:8000/docs

## Endpoints

- GET / - Root endpoint
- GET /health - Health check
- GET /docs - Swagger UI documentation

## Add packages as needed

```powershell
pip install <package-name>
pip freeze > requirements.txt
```

## Project Structure

```
backend/
 app/
    __init__.py
    main.py          # FastAPI app
 .env                 # Environment variables
 .gitignore          # Git ignore rules
 requirements.txt     # Dependencies
 README.md           # This file
```
