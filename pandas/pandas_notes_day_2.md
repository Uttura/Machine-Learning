# Day 2: Indexing, Selecting, and Assigning

### 1. Native Accessors (Python Style)
* **Code:** 
  ```python
  reviews['country']         # Bracket notation
  reviews.country            # Property notation
  reviews['country'][0]      # Specific element
  ```
* **My Mindset / Gotcha:** 
  * Dict-style indexing works because column names act as keys.
  * Property notation (`reviews.country`) is cleaner, but **fails if column names contain spaces** (e.g., `reviews.Country of Origin` breaks). Always default to brackets `['column_name']` when unsure.

---

### 2. Pandas Accessors: `iloc` vs `loc`
* **Rule #1:** Both are **[row, column]** first (opposite of standard Python which is column first).

#### A. Index-Based (`iloc`) — Position/Number Based
* **Code Examples:**
  ```python
  reviews.iloc[0]          # First row (all columns)
  reviews.iloc[:, 0]       # First column (all rows)
  reviews.iloc[:3, 0]      # First 3 rows of column 0
  reviews.iloc[1:3, 0]     # Rows 1 and 2 of column 0
  reviews.iloc[[0, 1, 2], 0] # Specific rows by index list
  reviews.iloc[-5:]        # Last 5 rows
  ```

#### B. Label-Based (`loc`) — Name Based
* **Code Examples:**
  ```python
  reviews.loc[0, 'country']
  reviews.loc[:, ['taster_name', 'points']]
  ```

* **CRITICAL DIFFERENCE (Index Slicing Gotcha):**
  * `iloc[0:1000]` $\rightarrow$ Returns **1000** rows (excludes index 1000, like standard Python lists).
  * `loc[0:1000]` $\rightarrow$ Returns **1001** rows (includes index 1000).

---

### 3. Index Manipulation
* **Code:** `reviews.set_index("title")`
* **My Mindset:** DataFrames aren't locked to numeric index numbers (`0, 1, 2...`). You can set any unique column (like titles or IDs) as the row index to make `.loc` searches easier.

---

### 4. Conditional Selection (Filtering Data)
* **Code Examples:**
  ```python
  # Basic single condition
  reviews.loc[reviews.country == 'Italy']

  # Multiple conditions (& = AND, | = OR)
  reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
  reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]

  # Built-in Helpers
  reviews.loc[reviews.country.isin(['Italy', 'France'])] # Value in list
  reviews.loc[reviews.price.notnull()]                   # Exclude NaNs / missing values
  ```
* **Note to Self:** Always wrap each condition in parentheses `(...)` when using `&` or `|` operators, or Python will raise a syntax error.

---

### 5. Assigning Data
* **Constant Value:** `reviews['critic'] = 'everyone'` (Fills entire column with 'everyone')
* **Iterated Value:** `reviews['index_backwards'] = range(len(reviews), 0, -1)`