# Day 6: Renaming and Combining

### 1. Renaming Columns & Indices (`rename` vs `rename_axis`)

* **Renaming Specific Labels (`rename()`):**
  ```python
  # Rename a column (very common) -> use a dictionary {'old_name': 'new_name'}
  reviews.rename(columns={'points': 'score'})

  # Rename specific row index labels (rarely needed)
  reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
  ```

* **Renaming the Index Headers (`rename_axis()`):**
  ```python
  # Name the row index axis and column index axis themselves
  reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')
  ```

* **My Mindset:** Use `rename()` to change the actual names *inside* your columns or rows. Use `rename_axis()` to label the index header row/column itself.

---

### 2. Combining DataFrames (`concat` vs `join`)

Pandas offers three main ways to combine data: `concat()`, `join()`, and `merge()` (most `merge()` tasks can be handled more easily with `join()`).

#### A. Stacking DataFrames (`concat()`)
* **My Mindset:** Think of `concat()` as **gluing/stacking** two tables with the exact same columns on top of each other (e.g., combining regional CSVs into one master dataset).
* **Code:**
  ```python
  canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
  british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")

  # Stack them together into a single DataFrame
  pd.concat([canadian_youtube, british_youtube])
  ```

#### B. Merging Side-by-Side on a Shared Index (`join()`)
* **My Mindset:** Use `join()` when you want to combine two different tables **side-by-side** based on a shared index (like matching videos trending on the same date in both countries).
* **Code:**
  ```python
  left = canadian_youtube.set_index(['title', 'trending_date'])
  right = british_youtube.set_index(['title', 'trending_date'])

  left.join(right, lsuffix='_CAN', rsuffix='_UK')
  ```
* **CRITICAL GOTCHA (`lsuffix` & `rsuffix`):**
  * Because both DataFrames share identical column names (like `views`, `likes`, etc.), `join()` will throw an error unless you tell Pandas how to differentiate them. Always pass `lsuffix` and `rsuffix` to tag which table each column came from!