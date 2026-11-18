# ML Part 2: Building Your First Machine Learning Model

### 1. Selecting Target (`y`) and Features (`X`)
* **Inspecting Available Columns:**
  ```python
  melbourne_data.columns
  ```
* **Prediction Target (`y`):** The single column we want to predict (by convention, always named lowercase `y`).
  ```python
  y = melbourne_data.Price
  ```
* **Features (`X`):** The list of input columns the model uses to make predictions (by convention, always named uppercase `X`).
  ```python
  melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
  X = melbourne_data[melbourne_features]
  ```
* **Quick Check:** Always run `X.describe()` and `X.head()` to verify the features look clean before feeding them into a model.

---

### 2. The 4-Step Scikit-Learn Modeling Workflow
Every model in `scikit-learn` (`sklearn`) follows this exact lifecycle: **Define $\rightarrow$ Fit $\rightarrow$ Predict $\rightarrow$ Evaluate**.

```python
from sklearn.tree import DecisionTreeRegressor

# 1. DEFINE: Choose model type and set random_state for reproducible results
melbourne_model = DecisionTreeRegressor(random_state=1)

# 2. FIT: Capture patterns from the training data (the heart of modeling)
melbourne_model.fit(X, y)

# 3. PREDICT: Make predictions on data
print(melbourne_model.predict(X.head()))
```

* **My Mindset / Pro-Tip (`random_state=1`):** ML models use controlled randomness when finding splits. Passing any fixed integer like `random_state=1` locks the random number generator so you get the exact same results every time you run your code (crucial for debugging and comparing changes).