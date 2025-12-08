# Copilot Instructions for Studio

## Project Overview

**Studio** is a Django 6.0 + React landing page and digital tool for small businesses. The architecture separates backend (Django API) from frontend (Vite + React).

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django 6.0, Django REST Framework, Python 3.12 |
| Frontend | React 18, Vite, TypeScript |
| UI Components | Radix UI primitives, Tailwind CSS, shadcn/ui patterns |
| Package Managers | uv (Python), npm (frontend) |
| Database | SQLite (dev), PostgreSQL (Railway prod) |
| Deployment | Railway (single service) |

## Project Structure

```
backend/            # Django backend
  ├── core/         # Django project config (settings, urls, wsgi/asgi)
  └── manage.py     # Django CLI entry point
frontend/           # React SPA (Vite)
  └── src/
      ├── components/   # Page sections (Hero, Services, Portfolio, etc.)
      │   └── ui/       # Reusable UI primitives (shadcn/ui style)
      ├── App.tsx       # Main app component
      └── main.tsx      # Entry point
```

## Developer Workflow

### Backend (Django)

```bash
uv sync                                     # Install Python dependencies
uv run python backend/manage.py migrate     # Apply migrations
uv run python backend/manage.py runserver   # Start API at http://127.0.0.1:8000
```

### Frontend (React)

```bash
cd frontend
npm install                          # Install dependencies
npm run dev                          # Start Vite dev server
npm run build                        # Production build to dist/
```

### Adding Dependencies

```bash
uv add <package>                     # Python production dependency
uv add --dev <package>               # Python dev dependency
cd frontend && npm install <pkg>     # Frontend dependency
```

## API Development

- Use Django REST Framework for all API endpoints
- API routes under `/api/` prefix in `core/urls.py`
- Serializers in `<app>/serializers.py`, ViewSets in `<app>/views.py`

## Conventions

### Django Apps

1. Create: `uv run python backend/manage.py startapp <appname>`
2. Move app folder into `backend/`
3. Register in `INSTALLED_APPS` in `backend/core/settings.py`
4. Include URLs in `backend/core/urls.py` using `include()`

### Frontend Components

- Page sections in `frontend/src/components/` (e.g., `Hero.tsx`, `Services.tsx`)
- Reusable UI primitives in `frontend/src/components/ui/` (Radix-based)
- Use `@/` path alias for imports (configured in `vite.config.ts`)
- API calls go through `frontend/src/lib/api.ts`

## Deployment (Railway)

Single service deployment: Django serves both API and static frontend.

**Railway auto-deploys using `railway.toml`:**
- Builds frontend, collects static files, runs migrations
- Starts gunicorn server

**Environment variables to set in Railway:**
- `SECRET_KEY` — Generate secure key: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
- `DEBUG=False`
- `ALLOWED_HOSTS=your-app.railway.app`
- `DATABASE_URL` — Auto-provided by Railway PostgreSQL addon

**Local production test:**
```bash
cd frontend && npm run build
uv run python backend/manage.py collectstatic --noinput
uv run python backend/manage.py runserver
# Visit http://127.0.0.1:8000
```

## Key Files

| File | Purpose |
|------|---------|
| `backend/core/settings.py` | Django configuration |
| `backend/core/urls.py` | API routing + SPA catch-all |
| `backend/landing_page/` | Main app (models, views, serializers) |
| `frontend/src/lib/api.ts` | API client with type definitions |
| `frontend/src/components/ui/` | Shared UI component library |
| `railway.toml` | Railway build/deploy config |
| `.env.example` | Environment variables reference |
