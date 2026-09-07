# Sixth Day of ML
## Dtypes and Messing Values
### Dtypes
- The data type for a column is dtype.
- `reviews.price.dtype`
- Results in the data type of `float64`.
- dtype returns the dtype of every column in the table
- like: reviews.dtype
- results in all the columns and it's type
- Data types means which way the data was stored initially.
- It's possible to change one column of one type to another.
- Using `astype()`, use values like `float64`, `int64` etc
- `reviews.points.astype('float64')`
- The dataframe or series index has its own dtype.
- `reviews.index.dtype`, results `dtype('int64')`

### Missing Values
- Entries missing values are given NAN, short for not a number, has float64 dtype by default( for technical reasons).
- pandas have function like `pd.isnull()` and `pd.notnull`
- `reviews[pd.isnull(reviews.country)]`
- replacing the missing value is a common operation.
- uses function like `fillna()`.
- It provides few different strats. First we can use it to replace `NaN` with `Unkonwn`.
- `reviews.region_2.fillna("Unknown")`
- Or we can have non-null value which we can replace with.
- If some one have a name in the entries but the user has already adept new name then we can replace old with new one.
- `reviews.taster_twitter_handle.replace("Kill", "killer")`
- `replace` function is quite handy while replacing values.
