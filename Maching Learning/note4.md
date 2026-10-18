# Eleventh Day of Machine Learning
## Model Validation
- We will evaluate almost every model we will ever built.
- In most(though not all) applications, the revelent measure of model quality is predicitive accuracy. In other words, will the model's prediction be close to what actually happens.
- Many of us make and will make  a huge mistake when measuring predictive accuract.
- This means that, they make prediction with the training data and compare those prediction with ti the target values in the training data.
- we will come across this problem with this aproach and will see how to solve it in a moment.
- Now, let's see how we do this first:
    First we need to summerize the model quality into understandable way. If you compare predicted and actual home values to predicted values for 10,000 houses,
    we will see both good and bad prediction but looking around 10,000 predicted and real data would be pointless.
    we need to summerize it into one  single metric
    - There are many metric for summarizing modal quality, but we will start with one called Mean Absolute Error(MEA).
- The prediction error for each house is:

    `error=actual−predicted`

    So, if a house cost $150,000 and you predicted it would cost $100,000 the error is $50,000.
    With the MAE metric, we take the absolute value of each error. This converts each error to a positive number. We then take the average of those absolute errors. This is our measure of model quality. In plain English, it can be said as

    On average, our predictions are off by about X.

To calculate MAE, we first need a model. That is built in a hidden cell below, which you can review by clicking the code button.
```
Data Loading Code Hidden Here
import pandas as pd
# Load data
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
# Filter rows with missing price values
filtered_melbourne_data = melbourne_data.dropna(axis=0)
# Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]
from sklearn.tree import DecisionTreeRegressor
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(X, y)
```


Once we have a model, here is how we calculate the mean absolute error:

from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)

## The Problem with "In-Sample" Scores

- The measure we just computed can be called an "in-sample" score. We used a single "sample" of houses for both building the model and evaluating it. Here's why this is bad.

- Imagine that, in the large real estate market, door color is unrelated to home price.

- However, in the sample of data you used to build the model, all homes with green doors were very expensive. The model's job is to find patterns that predict home prices, so it will see this pattern, and it will always predict high prices for homes with green doors.

- Since this pattern was derived from the training data, the model will appear accurate in the training data.

- But if this pattern doesn't hold when the model sees new data, the model would be very inaccurate when used in practice.

- Since models' practical value come from making predictions on new data, we measure performance on data that wasn't used to build the model. The most straightforward way to do this is to exclude some data from the model-building process, and then use those to test the model's accuracy on data it hasn't seen before. This data is called validation data.

## Coding It

The scikit-learn library has a function train_test_split to break up the data into two pieces. We'll use some of that data as training data to fit the model, and we'll use the other data as validation data to calculate mean_absolute_error.

Here is the code:
```
from sklearn.model_selection import train_test_split
# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to the random_state argument gurantees we get the dame split every timewe run this script.
train_X, val_X, train_y,val_y = train_test_split(X,Y,random_state = 0)
#Define model
melbourne_model = DecisionTreeRegressor()
# Fit Model
melbourne_model.fit(train_X,train_y)
#get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
```

    