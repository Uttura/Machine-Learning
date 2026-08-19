# Fist day of Machine Learinig
## Creating, Reading and Writing

### Importing pandas library
    `import pandas as pd`

### Creating Data
There are two core object in pandas: the Dataframe and The series.

#### DataFrame
- A dataframe is a table.
- Conatains an array of induvidual entities, each of which has a certain value.
- Each entry corresponds to a row(or record) and a column.
- for example consider the following simple data frame:
    In[2]:
    `pd.DataFrame({'Yes':[50,21],'NO':[131,2]})`
    Out[2]:
    | |Yes|No |
    |0|50 |131|
    |1|21 |2  |
In this example,
`the value of the index or cord ( 0, yes) is 50 and for index or cord (0,No) is 131 and soon.`

##### Note:
- DataFrame entries are not limited to integers.
    `pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})`
    Out[3]:
    	Bob 	        Sue
    0 	I liked it. 	Pretty good.
    1 	It was awful. 	Bland.

##### Explanation of DataFrame
`pd.DataFrame()` is a constructor used to generate theses DataFrame objects. The syntax for declaring a new one is a dictionary whose keys arre the column names and whose values are a list of entries (Like: `{'columns_name': [values in the list],....}`). This is the standard way of constructing a new DataFrame, and it is what we encounter the most.

##### Specification of rows
    In the dictionary-list constructor, it assigns values to the column labels, but just uses an ascending cound from 0( 0,1,2,3,...) for the row labels itself.

    The list of row labels used in DataFrame is known as Index. We can assign value to it by using an index parameter in out consturctor:
- `pd.DataFrame({'bob':['ok','not ok'],'sue':['pretty good','Bland']},index=['Product A', 'Product B'])`
    It's output:
             	Bob 	        Sue
    Product A 	I liked it. 	Pretty good.
    Product B 	It was awful. 	Bland.


#### Series
- A series is a sequence of data vlaue. This means it is just a list. creating a series required nothing else then a list.
In[5]:
- `pd.Series([1,2,3,4,5])`
Out[5]:
    0    1
    1    2
    2    3
    3    4
    4    5
    dtype: int64
##### Explanation on Series

We can think of this as single column of the dataframe.
We can asign the row lebes using the index paramater as we did in the DataFrame but a series doesnot have a column name( it only have one overall name).
In[6]:
`pd.Series([30,35,40],index = ['2014 sales','2015 sales','2016 sales'], name='Product A')`
out[6]:
    2015 Sales    30
    2016 Sales    35
    2017 Sales    40
    Name: Product A, dtype: int64

##### Note
-    `Just think of DataFrame as a bunch of Series " glued together".`


### Reading data files

- Creating a Dataframe or series by hand is handy. But, most of the time we will work with existing data.

- The data can be sorted in ant form or way. but, commonly and the most basic of these is the humble CSV file.

- Comma-seperated Values (CSV) as it's name it is a file in table format with values being seperated by comma.

- we use `pd.read_csv()` function to read the data into a DataFrame.

IN[7]:
- `wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")`
- we can use shape attribute to check how large the resulting data frame is:
For example:
    IN[8]:
    wine_reviews.shape
    Out[8]:
    (129971,14)

    Here, out new DataFrame has 120000 records split acreoo 14 different columns. That's almost 2 million entries!
- we can examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows:
IN[9]:
- `wine_reviews.head()`
Out[9]:
 	Unnamed: 0 	country 	description 	designation 	points 	price 	province 	region_1 	region_2 	taster_name 	taster_twitter_handle 	title 	variety 	winery
0 	0 	Italy 	Aromas include tropical fruit, broom, brimston... 	Vulkà Bianco 	87 	NaN 	Sicily & Sardinia 	Etna 	NaN 	Kerin O’Keefe 	@kerinokeefe 	Nicosia 2013 Vulkà Bianco (Etna) 	White Blend 	Nicosia
1 	1 	Portugal 	This is ripe and fruity, a wine that is smooth... 	Avidagos 	87 	15.0 	Douro 	NaN 	NaN 	Roger Voss 	@vossroger 	Quinta dos Avidagos 2011 Avidagos Red (Douro) 	Portuguese Red 	Quinta dos Avidagos
2 	2 	US 	Tart and snappy, the flavors of lime flesh and... 	NaN 	87 	14.0 	Oregon 	Willamette Valley 	Willamette Valley 	Paul Gregutt 	@paulgwine 	Rainstorm 2013 Pinot Gris (Willamette Valley) 	Pinot Gris 	Rainstorm
3 	3 	US 	Pineapple rind, lemon pith and orange blossom ... 	Reserve Late Harvest 	87 	13.0 	Michigan 	Lake Michigan Shore 	NaN 	Alexander Peartree 	NaN 	St. Julian 2013 Reserve Late Harvest Riesling ... 	Riesling 	St. Julian
4 	4 	US 	Much like the regular bottling from 2012, this... 	Vintner's Reserve Wild Child Block 	87 	65.0 	Oregon 	Willamette Valley 	Willamette Valley 	Paul Gregutt 	@paulgwine 	Sweet Cheeks 2012 Vintner's Reserve Wild Child... 	Pinot Noir 	Sweet Cheeks

- The pd.read_csv() fucntion is well endowed, with over 30 optional parameters we can specify. For example, you can see in this dataset that the csv files has a build in index, which pandas didnot pick on automatically. To make panda use the existing index we can specify an index_col.

In[10]:
wine_reviews = pd.read_csv("../input/wine_reviews/filename.csv", index_col=0)
wine_reviews.head()
Out[10]:
 	country 	description 	designation 	points 	price 	province 	region_1 	region_2 	taster_name 	taster_twitter_handle 	title 	variety 	winery
0 	Italy 	Aromas include tropical fruit, broom, brimston... 	Vulkà Bianco 	87 	NaN 	Sicily & Sardinia 	Etna 	NaN 	Kerin O’Keefe 	@kerinokeefe 	Nicosia 2013 Vulkà Bianco (Etna) 	White Blend 	Nicosia
1 	Portugal 	This is ripe and fruity, a wine that is smooth... 	Avidagos 	87 	15.0 	Douro 	NaN 	NaN 	Roger Voss 	@vossroger 	Quinta dos Avidagos 2011 Avidagos Red (Douro) 	Portuguese Red 	Quinta dos Avidagos
2 	US 	Tart and snappy, the flavors of lime flesh and... 	NaN 	87 	14.0 	Oregon 	Willamette Valley 	Willamette Valley 	Paul Gregutt 	@paulgwine 	Rainstorm 2013 Pinot Gris (Willamette Valley) 	Pinot Gris 	Rainstorm
3 	US 	Pineapple rind, lemon pith and orange blossom ... 	Reserve Late Harvest 	87 	13.0 	Michigan 	Lake Michigan Shore 	NaN 	Alexander Peartree 	NaN 	St. Julian 2013 Reserve Late Harvest Riesling ... 	Riesling 	St. Julian
4 	US 	Much like the regular bottling from 2012, this... 	Vintner's Reserve Wild Child Block 	87 	65.0 	Oregon 	Willamette Valley 	Willamette Valley 	Paul Gregutt 	@paulgwine 	Sweet Cheeks 2012 Vintner's Reserve Wild Child... 	Pinot Noir 	Sweet Cheeks







