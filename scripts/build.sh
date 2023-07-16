#!/bin/bash
set -euxo pipefail


if [ "$RUN_ENV" = "production" ]; then
    pip install torch==1.13.1+cpu torchvision==0.14.1+cpu --extra-index-url https://download.pytorch.org/whl/cpu
fi

poetry lock
poetry config virtualenvs.create false

poetry install --no-interaction --no-ansi
poetry add python-multipart --no-interaction --no-ansi