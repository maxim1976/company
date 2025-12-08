# Use Python 3.12 slim image
FROM python:3.12-slim

# Install system dependencies including PostgreSQL client
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js 20 for frontend build
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Set work directory
WORKDIR /app

# Copy Python dependencies first for better caching
COPY pyproject.toml uv.lock ./

# Install Python dependencies
RUN uv sync --frozen --no-dev

# Copy the rest of the application
COPY . .

# Build frontend
RUN cd frontend && npm install && npm run build

# Collect static files
RUN uv run python backend/manage.py collectstatic --noinput

# Expose port
EXPOSE 8080

# Start the application
CMD cd backend && uv run gunicorn core.wsgi --bind 0.0.0.0:$PORT