#!/bin/bash
set -euxo pipefail

poetry lock
poetry config virtualenvs.create false

if [ "$RUN_ENV" = "production" ]; then
  poetry add torch --no-interaction --no-ansi --optional --platform linux --python ">=3.9 <3.10" --url "https://download.pytorch.org/whl/cpu/torch-1.13.1%2Bcpu-cp39-cp39-linux_x86_64.whl"
  poetry add torchvision --no-interaction --no-ansi --optional --platform linux --python ">=3.9 <3.10" --url "https://download.pytorch.org/whl/cpu/torchvision-0.14.1%2Bcpu-cp39-cp39-linux_x86_64.whl"
fi

poetry install --no-interaction --no-ansi
poetry add python-multipart