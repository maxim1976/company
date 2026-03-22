# Studio

A lightweight web studio landing page and digital tool for small businesses.

## Tech Stack

- **Backend:** Django 6, Django REST Framework
- **Database:** SQLite (local), PostgreSQL (production)
- **Package manager:** [uv](https://docs.astral.sh/uv/)

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) — no manual venv needed, `uv` manages it automatically

## Local Development

### 1. Install dependencies

```bash
cd studio
uv sync
```

This creates/updates `.venv` and installs all packages from `pyproject.toml`.

### 2. Run the development server

```bash
uv run python backend/manage.py runserver
```

Server starts at **http://127.0.0.1:8000/**

### 3. (Optional) Run migrations

```bash
uv run python backend/manage.py migrate
```

### 4. (Optional) Seed sample data

```bash
uv run python backend/seed_data.py
```

### 5. (Optional) Create a superuser

```bash
uv run python backend/manage.py createsuperuser
```

Admin panel: **http://127.0.0.1:8000/admin/**

## Running with a custom port

```bash
uv run python backend/manage.py runserver 8080
```

## Environment Variables

Create a `.env` file in the `studio/` directory for local overrides:

```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

## Deployment

See [RAILWAY_DEPLOYMENT.md](RAILWAY_DEPLOYMENT.md) for Railway deployment instructions.
uv
