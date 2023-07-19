#!/bin/bash
set -euxo pipefail

# gunicorn translation.asgi:app -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker --reload
python run.py