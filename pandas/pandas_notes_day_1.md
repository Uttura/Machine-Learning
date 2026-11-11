# Day 1: Pandas — Creating, Reading, and Writing

### 1. Importing & Core Objects
* **Code:** `import pandas as pd`
* **My Mindset / Core Idea:** Pandas revolves around two primary data structures:
  * **DataFrame:** A 2D table (think of it like an Excel sheet or SQL table with rows and columns).
  * **Series:** A 1D sequence of values (think of it as a single column of a DataFrame).

---

### 2. Creating Data & Custom Indices
* **DataFrame Syntax:** 
  ```python
  pd.DataFrame({
      'Bob': ['I liked it.', 'It was awful.'], 
      'Sue': ['Pretty good.', 'Bland.']
  }, index=['Product A', 'Product B'])
  ```
* **Series Syntax:** 
  ```python
  pd.Series([30, 35, 40], index=['2014 Sales', '2015 Sales', '2016 Sales'], name='Product A')
  ```
* **My Mindset / Note to Self:** 
  * Dict keys become **column names**, and lists become **data entries**. 
  * By default, row labels (the index) auto-number from `0, 1, 2...`. Override this using the `index=[...]` parameter. 
  * *Mental shortcut:* A DataFrame is literally just a bunch of Series "glued together" sharing the same index.

---

### 3. Reading Data Files (CSV)
* **Code:** 
  ```python
  wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")
  ```
* **Inspecting Data:**
  * `wine_reviews.shape` $\rightarrow$ Checks dimensions `(rows, columns)`.
  * `wine_reviews.head()` $\rightarrow$ Grabs the first 5 rows to quickly preview what the columns look like.
* **Pro-Tip / Gotcha (`index_col`):**
  * If the CSV file already contains a built-in ID or row column that Pandas turns into an unwanted `Unnamed: 0` column, fix it immediately on load by specifying `index_col=0`:
  ```python
  wine_reviews = pd.read_csv("filename.csv", index_col=0)
  ```