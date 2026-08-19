# Second day of Machine Learning
## Indexing, Selecting and Assigning

### Native accessors
- Standard python objects provide good way of indexing data.
- Pandas carries all of these over, which helps make it easy to start with.
- Consider one dataframe with data as usual:
    now just think how you will address or call out one sepcific part of the dictionary in standard python
    `dict_name[key]` as in dictionary we call it key value pair.
    In this dataframe example, the key would be the desired column_name and the value would be the list for the given key.
    Just think of that as you have got a dataframe named something ( that name would be the dictionary name and the column name (key) would be the property of that dict). Making the call easier like `reviews['country]` or `reviews.country`.
    In terms of syntaxing, both are perfect but using the `reviews.country` might not be very handy due to one problem.
    For Example:
        if the name of the column name ( key) is `Country of Origin` then the normal dict form won't have any problem `reviews['Country of Origin']`, but this property defining way won't work `reviews.Country of Origin`. This will create error like `of was not defined and Origin was not define`.
    Some basic dict nest indexing would be:
        `reviews['Country Of origin'][0]` --> This specify the first element of the column `Counrty of origin`.

### Indexing
Indexing operator and attribute selection are nice because they work just like they do in the rest of the python ecosystem. However, pandas has it's own accessor operators, `loc` and `iloc`. For more advanced operations, these are the one we're supposed to be using.

#### Index-dased selection
- Pandas indexing works in one of two paradigms. First one is index-based selection:
    selecting data based on it's numerical position in data iloc follows this paradigm.
- To select the first row of data in a dataFrame, we may use the following:
    `reviews.iloc[0]`
    output is whole row in index zero is populated.
- Both loc and iloc are row-first, column-second. This is the opposite of what we bo in native in python, which is column first, row-second.
- This simply means it is easier to retrive rows and harder to retrice columns. 
- To get a column with iloc, we can do the following:
    `reviews.iloc[:, 0]`
    now it's output would be the whole column in the index 0.
- The operator : comes from native python, it means "Everything". When combined with other selectors,it can be used to indicate a range of values. For example, to select the country comumn from the first second and third row , we can do this:
    `reviews.iloc[:3, 0]`
    The output is the first three rows in country column
- Not only that, we can even specify the interval like if you want second and third entries then we can do this:
    `reviews.iloc[1:3, 0]` here the value before colon represent the value from which this operation has to include and the value after the colon represent from  which this operation has to exclude entries( one got exclude and only 1 and 2 are populate).
- We can even use list for it:
    `review.iloc[[0,1,2],0]`
- We can even populate DataFrame from backward using negative values:
    `reviews.iloc[-5:]`
    This will populate the data of the last five entries.
#### Label-based selection
- The second paradigm for attribute selection is the one followed by loc operator.
- This is a data index value not position based.
- for ecample, to get the first entry in reviews, we would now do the following:
    `reviews.loc[0, 'country']`
    the output is the first value in hte country column
- Despite iloc being conceptually simpler, we use loc for easiness, becuase the loc works with names which in real data entries would have some meaning and make the reading and context of data more clear. for example:
    `reviews.loc[:, ['tester_name', 'taster_twitter_handle', 'points']]`
- One main point to remember:
    `x.loc[0:1000]` return 1001 entries include 1000
    `x.iloc[0:1000]` return 1000 entries exclude 1000

### Manipulation the index
- Label-based selection derives its power from the labels in the index.
- The index we use is not immitable
