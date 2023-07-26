"""
Usage:
- Run app: python run.py
- Generate openapi docs: python run.py openapi
"""
import os
import uvicorn

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

# def label_breed(x): 
#     filename = x.split('/')[-1]  # Extract the file name from the path if applicable
#     label = ' '.join(word.capitalize() for word in filename.split('_')[:-1])  # Remove the last part (number) after the last underscore
#     return label

def is_cat(x): return x[0].isupper() 

if __name__ == "__main__":
    uvicorn.run("asgi:app", port=8000, host="0.0.0.0", reload=True)
