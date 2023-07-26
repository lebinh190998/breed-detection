from fastai.vision.all import *
import os

# Construct the absolute file path
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pkl_file_path = os.path.join(base_path, 'breed_identifier_model.pkl')

async def predict(image) -> str:
    print("---- LOADING LEANER ----")
    learn = load_learner(pkl_file_path, cpu=True)
    
    # Load the .pkl file
    print("---- OPENING IMAGE ----")
    im = Image.open(image.file)
    im.thumbnail((192,192))
    print("---- PREDICTING ----")
    (pred, idx, probs) = learn.predict(im)

    return pred