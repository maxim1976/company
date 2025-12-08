#!/bin/bash
set -e

# Build frontend
cd frontend
npm install
npm run build
cd ..

# Django setup
uv run python backend/manage.py collectstatic --noinput
uv run python backend/manage.py migrate

# Start server
cd backend
exec gunicorn core.wsgi --bind 0.0.0.0:${PORT:-8000}
