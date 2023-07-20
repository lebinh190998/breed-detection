from fastai.vision.all import *
import os

def label_breed(x): 
    filename = x.split('/')[-1]
    label = ' '.join(word.capitalize() for word in filename.split('_')[:-1])
    return label


# Construct the absolute file path
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
experiment_directory = os.path.join(base_path, 'experiment')
pkl_file_path = os.path.join(experiment_directory, 'breed_identifier_model.pkl')

print("---- LOADING LEANER ----")
learn = load_learner(pkl_file_path, cpu=True)

async def predict(image) -> str:
    # Load the .pkl file
    print("---- OPENING IMAGE ----")
    im = Image.open(image.file)
    im.thumbnail((192,192))
    print("---- PREDICTING ----")
    (pred, idx, probs) = learn.predict(im)

    return pred