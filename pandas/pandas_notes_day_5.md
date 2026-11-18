# Day 5: Data Types (Dtypes) and Missing Values

### 1. Data Types (`dtypes`)

* **My Mindset:** `dtype` tells you how Pandas stores a column under the hood (e.g., `int64`, `float64`, or `object` for strings).

* **Code Examples:**
  ```python
  reviews.price.dtype               # Check a single column -> dtype('float64')
  reviews.dtypes                    # Check ALL columns in the DataFrame
  reviews.index.dtype               # Even the index has its own dtype -> dtype('int64')

  # Convert a column from one type to another
  reviews.points.astype('float64')
  ```

* **Note to Self:** Remember `.dtype` (singular) is for a single Series/column, while `.dtypes` (plural) checks the entire DataFrame at once.

---

### 2. Handling Missing Values (`NaN`)

* **My Mindset / Technical Gotcha:** Missing entries are marked as `NaN` (*Not a Number*). For internal technical reasons, Pandas always assigns `NaN` values a `float64` dtype.

* **Finding Missing Data (`isnull` / `notnull`):**
  ```python
  # Filter and view only the rows where 'country' is missing
  reviews[pd.isnull(reviews.country)]
  ```
  *(Use `pd.notnull()` for the exact opposite—filtering out empty rows).*

* **Filling Missing Data (`fillna`):**
  ```python
  # Replace all NaN values with a fallback string
  reviews.region_2.fillna("Unknown")
  ```

---

### 3. Replacing Existing Values (`replace`)

* **Code:**
  ```python
  # Swap an outdated non-null value for a new one (e.g., updated Twitter handles or typos)
  reviews.taster_twitter_handle.replace("Kill", "killer")
  ```

* **My Mindset:** Use `fillna()` specifically when targeting missing `NaN` entries, and reach for `replace()` whenever you need to update existing, non-empty values across a column.