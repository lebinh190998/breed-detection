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

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def label_breed(x): 
    filename = x.split('/')[-1]  # Extract the file name from the path if applicable
    label = ' '.join(word.capitalize() for word in filename.split('_')[:-1])  # Remove the last part (number) after the last underscore
    return label

print("---- LOADING LEANER ----")
pkl_file_path = os.path.join(CURRENT_DIR, 'breed_identifier_model.pkl')
learn = load_learner(pkl_file_path, cpu=True)

if __name__ == "__main__":
    uvicorn.run("asgi:app", port=8000, host="0.0.0.0", reload=True)
