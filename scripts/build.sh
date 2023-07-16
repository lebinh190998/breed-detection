#!/bin/bash
set -euxo pipefail

poetry lock
poetry config virtualenvs.create false

if [ "$RUN_ENV" = "production" ]; then
  python3 -m pip install --no-cache-dir torch==1.13.1+cpu -f "https://download.pytorch.org/whl/cpu/torch_stable.html"
  python3 -m pip install --no-cache-dir torchvision==0.14.1+cpu -f "https://download.pytorch.org/whl/cpu/torch_stable.html"
fi

poetry install --no-interaction --no-ansi
poetry add python-multipart --no-interaction --no-ansi