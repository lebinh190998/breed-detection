from fastai.vision.all import *
from run import learn
import os

# Construct the absolute file path
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pkl_file_path = os.path.join(base_path, 'breed_identifier_model.pkl')

async def predict(image) -> str:
    # Load the .pkl file
    print("---- OPENING IMAGE ----")
    im = Image.open(image.file)
    im.thumbnail((192,192))
    print("---- PREDICTING ----")
    (pred, idx, probs) = learn.predict(im)

    return pred