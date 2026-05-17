import pytest

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country"
]

data = pd.read_csv("data/census.csv")

train, test = train_test_split(data, test_size=0.20)

X_train, y_train, encoder, lb = process_data(
    train,
    categorical_features=cat_features,
    label="salary",
    training=True
)

X_test, y_test, _, _ = process_data(
    test,
    categorical_features=cat_features,
    label="salary",
    training=False,
    encoder=encoder,
    lb=lb
)

model = train_model(X_train, y_train)


def test_model_type():
    """
    ensure model is using RandomForestClassifier
    """
   
    assert isinstance(model, RandomForestClassifier)


def test_inference_size():
    """
    test that the inference returns the same number of predictions as number of rows passed in
    """
    preds = inference(model, X_test)

    assert len(preds) == len(X_test)


def test_prediction_values():
    """
    # Tests if predictions return only 0 or 1
    """
    preds = inference(model, X_test)

    assert set(preds).issubset({0,1})
