FROM python:3.12-slim-bookworm

# Use uv as the package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy only requirements first to optimize caching
COPY pyproject.toml requirements.txt ./

# Initialize virtual environment and install dependencies
RUN uv venv
RUN uv sync --frozen

# Now copy the rest of the app
COPY . .

EXPOSE 8000

# Run the server
CMD ["uv", "run", "manage.py", "runserver", "0.0.0.0:8000"]