# Forth Days of ML
## Summary Functions and Maps
### Summary Functions
- Pandas provide some useful summery function ( it is just generalized name not some official name) which restructure the data in some useful way.
- `describe()` method:
    `reviews.points.describe()`

    output is the high level summery of given column. like in this case:
        the no of entries in points column,
        mean of the all the given output
        percentage wise representation
        and an maximum value in the column
- In the above, the describe function make sense for numerical data only.
- `reviews.tester_name.describe()` this only shows summery like count, unique, top and freq which are not a worth full summery.
- You can even specify what kind of summery you want like :
    `reviews.points.mean()` this is to know only the mean of the points column
    `reviews.tester_name.unique()` this to see the list of unique values
    `reviews.tester_name.value_counts()` this is to see a list of unique values and how often they occur in the dataset.

### Maps
- This is a term borrowed from maths, for a function that takes one set of values and maps them to another set of values.
- In data science we often have a need for creating new representations from existing data, or for transforming data from the formate it is in now to formate that we want it to be in later.
- Maps are what handle this work, making them extremely important for getting your work done!
- There are two methods that we will use often `map()` and `apply()`.
#### Map()
- This is the first and the slightly simpler one.
- For example, suppose that we wanted to remean the scores the wines received to 0. We can do the following:
    `review_points_mean = reviews.points.mean(),`
    `reviews.points.map(lamda p:p - review_points_mean)`
- Explaination of above example:
    The function we pass to map() should expect a single value from the series( a point value, in the above example), and return a transformed version of that value. map() returns a new series where all the values have been transformed by our function.
### Apply()
- `apply()` is the equivalent method if we want to transform a whole dataframe by calling a coustom method on each row.
- For example:
    ` def remean_points(row):`
        `row.points = row.points-reviews_points_mean`
        `return row`
    `reviews.apply(remean_points,asis='columns')`
- If we had called reviews.apply() with axis='index, then instead of passing a function to transform wach row, we would need to give a function to transform each column.
- Note:
    The `map()` and `apply()` returns new, transformed series and Dataframes, respectively. They don't modify the original data they're called on. If we look at the first row of reviews, we can see that it still has its original points value.
- `reviews.head(1)`
- Pandas provide very common mapping operations as built-ins.like:
    `revies_points_mean = reviews.points.mean()`
    `reviews.points - review_points_mean`
    In this code we are performing an operation between a lot of values on the left-hand side( everything in the series) and a single value on the right-hand side(the mean value). Pandas looks at this expression and figures out that we must mean to subtract that mean value from every value in the dataset.
    Pandas will also understand what to do if we perform these operations between series of equal length. For example, an esay way of combining country and region information in the dataset would be to do the following:
        `reviews.country + " - " + reviews.region_1`
        this return value in `Country - region`
    these operators are faster then both map() and apply() because they use speed ups built into pandas. All the standard python operators (>, <, ==, and so on) works in this manner.
    However they are not as fexible as map() or apply(), which can do more advanced things, like apply conditional logic. which cannot be done with addition and substraction.





