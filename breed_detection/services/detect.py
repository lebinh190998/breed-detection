from fastai.vision.all import *
import os
import torch

# Construct the absolute file path
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
experiment_directory = os.path.join(base_path, 'experiment')
pkl_file_path = os.path.join(experiment_directory, 'breed_identifier_model.pkl')

async def predict(image) -> str:
    # Load the .pkl file
    with open(pkl_file_path, 'rb') as f:
        learn = torch.load(f)

    im = Image.open(image.file)
    im.thumbnail((192,192))
    (pred, idx, probs) = learn.predict(im)
    return pred