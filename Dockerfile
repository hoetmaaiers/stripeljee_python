FROM python:3.12.1
LABEL authors="robin"

# Ensure pip, setuptools, and wheel are up to date
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install Poetry
RUN pip install --no-cache-dir poetry

WORKDIR /app

# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml README.md ./

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copying in our source code
COPY . .

EXPOSE 8000

CMD ["python", "stripeljee_python/main.py"]

