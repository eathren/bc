# Use the official Python image from the Docker Hub
FROM python:3.13.1-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.8.5

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files to the container
COPY pyproject.toml poetry.lock /app/

# Install the dependencies
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copy the rest of the application code to the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]