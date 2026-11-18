# ML Part 3: Model Validation

### 1. Measuring Quality: Mean Absolute Error (MAE)
* **My Mindset:** Looking at 10,000 individual predictions vs. actual prices is useless—we need a single number summarizing how wrong our model is.
* **Formula:**
  $$\text{Error} = |\text{Actual} - \text{Predicted}|$$
  **MAE** takes the absolute value of every error (so negative and positive errors don't cancel out) and averages them. In plain English: *"On average, our predictions are off by about X dollars."*
* **Code:**
  ```python
  from sklearn.metrics import mean_absolute_error

  predicted_home_prices = melbourne_model.predict(X)
  mean_absolute_error(y, predicted_home_prices)
  ```

---

### 2. The "In-Sample" Score Trap
* **CRITICAL GOTCHA:** Never evaluate a model using the exact same data you trained it on!
* **Why? (The Green Door Analogy):** Suppose in your training data, every house with a green door happened to be a mansion. A Decision Tree will memorize *"green door = expensive"*, scoring near 0 error on the training data. When deployed on new real-world houses, that fake pattern fails completely.

---

### 3. The Solution: Train / Validation Split (`train_test_split`)
* **My Mindset:** Hide a chunk of data during training (`val_X`, `val_y`), then test the model on that unseen data to see how it actually performs in the real world.
* **Complete Validation Code:**
  ```python
  from sklearn.model_selection import train_test_split
  from sklearn.tree import DecisionTreeRegressor
  from sklearn.metrics import mean_absolute_error

  # Split data into training and validation sets
  train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

  # Define and fit ONLY on training data
  melbourne_model = DecisionTreeRegressor(random_state=1)
  melbourne_model.fit(train_X, train_y)

  # Predict and evaluate ONLY on unseen validation data
  val_predictions = melbourne_model.predict(val_X)
  print(mean_absolute_error(val_y, val_predictions))
  ```