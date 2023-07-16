#!/bin/bash
set -euxo pipefail

poetry lock
poetry config virtualenvs.create false

if [ "$RUN_ENV" = "production" ]; then
    poetry install --no-interaction --no-ansi --config pyproject.prod.toml
else
    poetry install --no-interaction --no-ansi --config pyproject.dev.toml
fi

poetry add python-multipart --no-interaction --no-ansi