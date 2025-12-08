# Use Python 3.12 slim image
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js 18 for frontend build
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Install uv
RUN pip install uv

# Set work directory
WORKDIR /app

# Copy Python dependencies first for better caching
COPY pyproject.toml uv.lock ./

# Install Python dependencies
RUN uv sync --frozen --no-install-project --no-dev

# Copy the rest of the application
COPY . .

# Build frontend
RUN cd frontend && npm install && npm run build

# Collect static files and run migrations
RUN uv run python backend/manage.py collectstatic --noinput
RUN uv run python backend/manage.py migrate

# Expose port
EXPOSE 8000

# Start the application
CMD ["uv", "run", "gunicorn", "core.wsgi", "--bind", "0.0.0.0:8000"]