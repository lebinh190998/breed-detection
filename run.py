"""
Usage:
- Run app: python run.py
- Generate openapi docs: python run.py openapi
"""

import os
import sys
import uvicorn
import yaml
from fastai.vision.all import *
from breed_detection.asgi import app

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

path = untar_data(URLs.PETS)/'images'

def label_breed(x): 
    filename = x.split('/')[-1]  # Extract the file name from the path if applicable
    label = ' '.join(word.capitalize() for word in filename.split('_')[:-1])  # Remove the last part (number) after the last underscore
    return label

dls = ImageDataLoaders.from_name_func('.',
    get_image_files(path), valid_pct=0.2, seed=42,
    label_func=label_breed,
    item_tfms=Resize(192))

learn = vision_learner(dls, resnet18, metrics=error_rate)
# learn.fine_tune(4)

MODEL_PATH = os.path.join(CURRENT_DIR, 'breed_detection/breed_identifier_model.pkl')
learn.export(MODEL_PATH)

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
