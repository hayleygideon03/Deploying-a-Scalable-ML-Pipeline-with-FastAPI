# GitHub Repository:
https://github.com/hayleygideon03/Deploying-a-Scalable-ML-Pipeline-with-FastAPI

Working in a command line environment is recommended for ease of use with git and dvc. If on Windows, WSL1 or 2 is recommended.

# Environment Set up (pip or conda)
* Option 1: use the supplied file `environment.yml` to create a new environment with conda
* Option 2: use the supplied file `requirements.txt` to create a new environment with pip

This project was completed using option 1, using the 'environment.yml' file with Conda.

To create the environment:

''' bash
conda env create -f environment.yml
conda activate fastapi
'''
    
------------

# Repositories

I created a local git repository and connected it to GitHub. GitHub Actions was confirgured for CI/CD.

This GitHub Actions workflow:
- runs pytest
- runs flake8
- then automatically runs on pushes to main
- requires tests to pass successfully

-----------

# Data

This project uses the provided census.csv dataset

The dataset was cleaned and processed before the model was trained. The categorical columns were encoded using OneHotEnco
der and the labels were transformed using LabelBinarizer.

----------

# Model

Using the starter code, I created a ML model using a Random Forest Classifier from scikit-learn. The model trains on the census dataset, saves the trained model, saves the encodel and the label binarizer, then performs inference using FastAPI. 

Functionality is implemented in ml/model.py. The model training, model saving/loading, inference, the metric calculations, and performance evaluation on categorical slices.

Three unit tests were written and passed successfully

A function was created and written to slice_output.txt to show the model metrics for categorical features. This shows: 
- Precision: 0.7419
- Recall: 0.6384
- F1 Score: 0.6863

A model card is stored in model_card_template.md.

------------

# API Creation

A RESTful API was created using FastAPI.

This API implements:
    * GET on the root giving a welcome message.
    * POST that does model inference.

The API was tested locally using local_api.py

To run the API locally, run:
uvicorn main:app --reload

API documentation is available at - http://127.0.0.1:8000/docs

SCREENSHOTS:

Screenshots are located inside the GitHub repo
