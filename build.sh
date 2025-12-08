#!/bin/bash
set -e

echo "Building frontend..."
cd frontend
npm install
npm run build
cd ..

echo "Collecting static files..."
uv run python backend/manage.py collectstatic --noinput

echo "Running migrations..."
uv run python backend/manage.py migrate

echo "Build complete!"
