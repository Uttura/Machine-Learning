# Day 3: Summary Functions and Maps

### 1. Summary Functions

* **High-Level Overview (`describe()`):**

  * `reviews.points.describe()` $\rightarrow$ Generates count, mean, std, min, max, and percentiles for numerical columns.

  * `reviews.taster_name.describe()` $\rightarrow$ Generates count, unique, top, and frequency for string/categorical columns.

* **Specific Metrics (Individual Functions):**

  * `reviews.points.mean()` $\rightarrow$ Calculates average value.

  * `reviews.taster_name.unique()` $\rightarrow$ Array of unique values.

  * `reviews.taster_name.value_counts()` $\rightarrow$ List of unique values + how many times each appears.

### 2. Mapping Data (`map` vs `apply`)

Maps transform existing data into a new format. **Crucial Rule:** Neither `map()` nor `apply()` modifies the original DataFrame in place; they return a *new* transformed Series or DataFrame.

#### A. `map()` — For Single Series (1D)

* **Code:**

  ```python
  review_points_mean = reviews.points.mean()
  reviews.points.map(lambda p: p - review_points_mean)
  ```

* **My Mindset:** Takes a single value from a Series at a time, applies a function to it, and returns a transformed Series.

#### B. `apply()` — For Whole DataFrames (2D)

* **Code:**

  ```python
  def remean_points(row):
      row.points = row.points - review_points_mean
      return row

  reviews.apply(remean_points, axis='columns')
  ```

* **My Mindset / Gotcha (`axis` parameter):**

  * `axis='columns'` (or `1`) $\rightarrow$ Passes the function **row-by-row** (transforming values across columns for each row).

  * `axis='index'` (or `0`) $\rightarrow$ Passes the function **column-by-column**.

### 3. Built-in Vectorized Operations (Fastest)

* **Code Examples:**

  ```python
  # Subtracting a scalar from a Series
  reviews.points - review_points_mean

  # Combining two Series of equal length
  reviews.country + " - " + reviews.region_1
  ```

* **Pro-Tip / Performance Note:**

  * Always prefer built-in operators (`+`, `-`, `*`, `>`, `==`) over `map()` or `apply()` when doing standard math or string concatenation.

  * **Why?** Built-in operations use vectorized C-level code, making them significantly faster.

  * **When to use `map`/`apply`?** Only when complex conditional logic (like custom `if-else` functions) is required.