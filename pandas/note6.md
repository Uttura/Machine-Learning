# Senveth Day of ML
## Renaming and Combining
### Renaming
- In this the first function name is `rename()`.
- This lets us change the index names and/or column names.
- For example:
    To change the points column in our data sets to score, we would do:
    `reviews.rename(columns={'points': 'score'})`
- `rename()` lets us rename index or column values by specifying a variety of input formats, but usually python dictionary is the most convenient.
- For example:
    `reviews.rename(index={0: 'firstEntry', 1" 'secondEntry'})`
- We will rename the columns very often, but renaming index values would be rare.
- Both the column index and row index have their own attribute. The complimentary `rename_axis()` method may be used to change these name.
- For Example:
    `reviews.rename_axis("wines", axis='rows').rename_axis("fields,axis='column')`

### Combining
- while performing operations on a dataset, we will sometimes need to combine different DataFrames and/or Series in non-trival ways.
- There are three methods of combining the datasets.
- They are:
    `concat()`,`join()` and `merge()`.
- Most of what `merge()` can do, can be done more simply using  `join()`. so we will focused on `join()` and `concat()`.
- First, `concat()` is the simplest method. given a list of elements, this functionwill smush those elements together along an axis.
- For example:
    if you want to study about data which are seperated by country you can use this to concatinate the list or data to make one.
    `canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")`,
    `british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")`,
    `pd.concat([canadian_youtube,british_youtube])`
- `join()` is the middlemost combiner in terms of complexity.
- Lets you combine different Dataframe objects which have an index in common.
- For exmaple: 
    to pull down videos that happened to be trending on the smae day in both canada and the uk, we could do the following:
    `left = canadina_youtube.set_index(['title', 'trending_date'])`
    `right = british_youtube.set_index(['title', 'trending_date'])`
    `left.join(right,lsuffix='_CAN, rsuffix='_UK)`
- The `lsuffix` and `rsuffix` are necessary parameters cause this will need same columns name and if that was not true then we'd renamed them same 
