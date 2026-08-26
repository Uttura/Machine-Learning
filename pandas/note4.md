# Fifth day of Machine Learning
## Grouping and Sorting
### Groupwise analysis
- The most used function will be `value_counts()` function.
- We can replicate this function in the following way:
    `reviews.groupby('point').points.count()`
    The `groupby()` function create a group of reviews which allotted the same point values to the given wines.
    Then, for each of these groups, we grabbed the points() column and counted how many times it appeared.
    The `value_count()` is just a shortcut to this group operation.
- We can use any of the summery function we've used before with this data.
- For example,To get the cheapest wine in each point value category.we can do the following:
    `reviews.groupby('points).price.min()`
- Think of each group we generate as a slice of the dataframe containing only the data with values that match.
- In the same way as dataframe, we can access dataframe directly using `apply()` method.
- We can manipulate the data in any way we see fit.
- For example:
    `reviews.groupby('winery').apply(lambda df: df.title.iloc[0])`
    This can be used for selecting the name of the first wine reviewed from each winery in the dataset.
- To even fine-grained control, we can also group by more that one columns.
- For example:
    `reviews.groupby(['country','province'].apply(lambda df: df.loc[df.points.idxmax()]))`
    this is to pick out the best wine by country and province.
- Another `groupby()` method is `agg()`, this lets you run a bundh of differente functions on your dataframe simultaneously.
- For example:
    `reviews.groupby(['country']).price.agg([len,min,max])`
    used to generate a simple statistical summary of the dataset.

### Multi-indexes
- In all of examples, we used single-label index for dataframe or series. But `groupby()`is slightly different in the fact that , depending on the operation we run, it will sometimes result in what is called multi-index.
- A multi-index differs from a regular index in that it has multiple levels.
- For example:
    `countries_revirwed = reviews.groupby(['country','province']).desctiption.agg([len])`
    `countries_reviewed`
- `mi = countries_reviewed.index`
    `type(mi)`
    Output:
        pandas.core.indexes.multi.MultiIndex
- Multi-indices have several methods for dealing with their tiered structure which are absent for single-level indices.
- Also require two levels of labels to retrive a value.
- In general, multi-index method we will use most often is the one for converting back to a regular index, the `reset_index()` method:
    `countries_reviewed.reset_index()`
### Sorting
- The use of sorting functions. The `countries_reviewed`, the grouping returns data in index order not value order. That is to say, when outputting the result of a groupby, the order rows is dependent on the values in the index, not in the data.
- To get data in the order want it in we sort it ourself. The sort_values() method is handy for this:
    `countries_reviewed = countries_reviewed.reset_index()`
    `countries_reviewed.sort_values(by='len')`
- By default sort_values(), sort in ascending sort, where lowest value goes first. but most of the time we want the higher no to go first:
    `countries_reviewed.sort_values(by='len', ascending=False)`
- To sort index values, use `sort_index()`:
    `countries_reviewed.sort_index()`
- You can sort more then one column at a time:
    countries_reviewed.sort_values(by=['country','len'])
    