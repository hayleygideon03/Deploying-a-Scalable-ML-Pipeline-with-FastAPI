# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

For this model, I used a Random Forest Classifier to predict if a person makes more or less than $50,000 per year based on the census data provided. The goal of this project was to build a machine learning pipeline, train a model, and deploy that model using FastAPI. I also created unit tests, and an API endpoint that returns predictions from the trained model.



## Intended Use

This model was created for educational purposes. This project was made for the Udacity machine learning pipeline project. This project is not intended to make any real-world decisions.



## Training Data

This model was trained using the data provided from the census income dataset. This dataset contains information including age, education, occupation, sex, hours worked, and marital status. Categorical columns were encoded by using OneHotEncoder and then labels were transformed using LabelBinarizer.



## Evaluation Data

When evaluating the data, the data was split into training and testing datasets with a 80/20 train/test split. I used the test dataset to evaluate the model performance after testing was done.



## Metrics

*The model was evaluated using: Precision, Recall, and F1 Score. Here are the results:*



*Precision: 0.7419*



*Recall: 0.6384*



*F1 Score: 0.6863*



*The model was also evaluated on slices of data using different categorical features. This ouput is stored in slice\_output.txt.*



## Ethical Considerations

This dataset contains information such as race and sex, which could introduce bias compared to the original dataset. This could mean that the predictions are not fair across groups. That means this model should not be used in any formal decisions that could impact individuals.



## Caveats and Recommendations

This project was created mainly for educational purposes. The model is not highly optimized because the main focus of the project was learning how to build and deploy a machine learning pipeline.



Some limitations of this project include:



* possible bias in the dataset
* simple model setup
* minimal hyperparameter tuning



Possible improvements could include:



* testing additional models
* performing more detailed bias analysis
* improving feature engineering
* creating a more advanced deployment setup

