"""
Usage:
- Run app: python run.py
- Generate openapi docs: python run.py openapi
"""

import os
import sys
import uvicorn
import yaml

from breed_detection.asgi import app

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def label_breed(x): 
    filename = x.split('/')[-1]
    label = ' '.join(word.capitalize() for word in filename.split('_')[:-1])
    return label

if __name__ == "__main__":
    if sys.argv[-1] == "openapi":
        schema = app.openapi()
        path = os.path.join(CURRENT_DIR, "docs/openapi.yaml")
        yaml.Dumper.ignore_aliases = lambda *args: True
        with open(path, "w+") as f:
            yaml.dump(schema, f, default_flow_style=False)
        print(f"Saved docs at {path}")
    else:
        uvicorn.run("breed_detection.asgi:app", port=8000, host="0.0.0.0", reload=True)
