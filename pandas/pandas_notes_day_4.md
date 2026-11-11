# Day 4: Grouping and Sorting

### 1. Groupwise Analysis (`groupby`)

* **My Mindset:** Think of `groupby()` as creating mini "slices" or sub-DataFrames grouped by shared values. You can then run aggregations or functions on each slice.

* **Replicating `value_counts()`:**
  ```python
  reviews.groupby('points').points.count()
  ```
  *Note: `value_counts()` is just a convenient shortcut for this exact operation.*

* **Summary Functions on Groups:**
  ```python
  # Get the minimum price for each point category
  reviews.groupby('points').price.min()
  ```

* **Custom Functions with `apply()` on Groups:**
  ```python
  # Select the title of the first wine listed per winery
  reviews.groupby('winery').apply(lambda df: df.title.iloc[0])

  # Pick out the highest-rated wine entry per (country, province) group
  reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
  ```

* **Multiple Aggregations with `agg()`:**
  ```python
  # Run multiple statistical summary functions at the same time
  reviews.groupby(['country']).price.agg([len, 'min', 'max'])
  ```

---

### 2. Multi-Indexes & Flattening

* **My Mindset / Core Concept:** Grouping by multiple columns (e.g., `['country', 'province']`) creates a **MultiIndex**—a nested index with multiple levels.

* **Inspection:**
  ```python
  countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
  type(countries_reviewed.index)  # Returns pandas.core.indexes.multi.MultiIndex
  ```

* **Most Important Operation (`reset_index()`):**
  * MultiIndices can be tricky to query. Convert back to a standard flat DataFrame with `.reset_index()`:
  ```python
  countries_reviewed = countries_reviewed.reset_index()
  ```

---

### 3. Sorting Data (`sort_values` vs `sort_index`)

By default, `groupby` outputs rows ordered by the **index**, not by data values.

* **Sort by Values:**
  ```python
  # Ascending (default: lowest to highest)
  countries_reviewed.sort_values(by='len')

  # Descending (highest to lowest)
  countries_reviewed.sort_values(by='len', ascending=False)

  # Sort by multiple columns
  countries_reviewed.sort_values(by=['country', 'len'])
  ```

* **Sort by Index:**
  ```python
  countries_reviewed.sort_index()
  ```