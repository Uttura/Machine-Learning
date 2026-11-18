# ML Part 1: How Models Work & Basic Data Exploration

### 1. Decision Trees & How Models Work
* **My Mindset / Core Intuition:** Think of a Decision Tree like a flowchart that sorts data (like houses) into buckets based on features (rooms, bathrooms, location). The predicted price for any house is simply the **historical average** of past houses that landed in that same bucket.
* **Key Terminology:**
  * **Training / Fitting:** Feeding historical data into the model so it can figure out the best split points to separate the data into accurate buckets.
  * **Tree Depth / Features:** A simple tree looking at just 1 variable (e.g., *more than 2 bedrooms?*) gives a rough guess. Adding more features splits the buckets further, narrowing down the prediction.
  * **Leaf Node:** The final endpoint at the very bottom of the tree where the final predicted value is output.

---

### 2. Basic Data Exploration (Using Pandas)
* **My Mindset:** Before building any model, you have to inspect the raw dataset to see what columns exist, what values look like, and if anything is missing.
* **Core Workflow:**
  ```python
  import pandas as pd

  # Load dataset
  melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
  melbourne_data = pd.read_csv(melbourne_file_path)

  # Quick statistical summary of all numerical columns (count, mean, min, max, percentiles)
  melbourne_data.describe()
  ```
* **Note to Self:** Look closely at the `count` row in `.describe()`—if a column has a lower count than the total rows, it means there are missing values (`NaN`) we'll need to deal with before training!