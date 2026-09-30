# Tenth Day of Machine Learning
## My first MAchine learning models
### Selecting the Data For Modeling
- We will start by picking a few variables using our intuition.
- we will need to see a list of all columns in the dataset.
- That is done with the columns property of the dataframe
- `import pandas as pd`
- `melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.columns.csv'`
- `meldourne_data = pd.read_csv(melbourne_file_path)`
- `melbourne_data.columns`
- we will use two approaches from pandas for selecting supsets of our data:
    1. Dot notation, which we use to select the prediction target
    2. Selecting with a column list, which we use to select the features.
#### Selecting the prediction target
- We use the dot notation for the selection of the prediction target.
- The prediction target is nothing else than the column we want to predict.
- By convention, the prediction target is called y.
- So the code we need to save the house prices in the Melbourne data is :
    `y = melbourne_data.Price`
### Choosing "Features"
- The columns that are inputted into our model(and later used to make predictions) are called "Features." In our case. those would be the columns used to determine the home price. Sometimes, we will use all columns except the target as features. Other times you'll be better off with fewer features.
- For now, we'll build a model with only a few features. Leter on we'll see how to iterate and compare models built with different features.
- We select multiple features by providing a list of column names inside brackets. Each item in that list should be a string. Example:
    `melbourne_features=['Rooms','Bathroom','Landsize','Lattitude','Longtitude']`
- BY convention, this data is called X.
    `X = melbourne_data[melbourne_features]`
- Reviewing the data in the X dataframe we just created.
    `X.describe()`
    `X.head()`
### Building my Model
- We will use scikit-learn lib to create our models. we write it as sklearn while coding.
- The steps to building and using a model are:
    1. Define: What type of model will it be? A decision tree? Some other type of 2. model? Some other parameters of the model type are specified too.
    2. Fit: Capture patterns from provided data. This is the heart of modeling.
    3. Predict: Just what it sounds like
    4. Evaluate: Determine how accurate the model's predictions are.
- Example for how it is used foe defining a decision tree model with scikit-learn and fitting it with features and target variable.
    `from sklearn.tree impoer DecisionTreeRegressor`
    Defining model. Specify a number for random_state to ensure same result each run
    `melbourne_model = DecisionTreeRegressor(random_state=1)`
    Fit model
    `melbourne_model.fit(X,Y)`
- Many machine learning models allow some randomness in model training. Specifying a number for random_state ensures you get the same results in each run. This is considered a good practice. You use any number, and model quality won't depend meaningfully on exactly what value you choose.
- In practice, we want to make prediction for new houses comming on the market ranter that the houses we already have prices for. BUt we'll make predictions for the first few rows of the training data to see how the predict function works.
    `print("Making predictions for the following 5 houses:")`
    `print(X.head())`
    `print("The prediction are")`
    `print(melbourne_model.predict(X.head()))`

