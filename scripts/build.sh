#!/bin/bash
set -euxo pipefail

poetry lock
poetry config virtualenvs.create false

if [ "$RUN_ENV" = "production" ]; then
    # poetry add https://download.pytorch.org/whl/cpu/torch-1.13.1%2Bcpu-cp39-cp39-linux_x86_64.whl
    # poetry add https://download.pytorch.org/whl/cpu/torchvision-0.14.1%2Bcpu-cp39-cp39-linux_x86_64.whl

    poetry install --no-interaction --no-ansi --no-dev
else
    poetry install --no-interaction --no-ansi --no-dev
fi