#!/bin/bash
set -euxo pipefail

uvicorn breed_detection.asgi:app --host 0.0.0.0 --port 8000 --reload