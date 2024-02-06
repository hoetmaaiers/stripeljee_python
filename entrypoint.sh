#!/bin/bash

# Load environment variables from .env file
set -a
source .env
set +a

# Run Alembic migrations
alembic upgrade head

# Start your application
exec "$@"
