
# coding: utf-8
# # Creating Data

import pandas as pd

pd.DataFrame({'Yes': [50,21], 'No': [131, 2]})  # DataFrame with integers

# DataFrame with strings
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.','Bland.']})

# We can assign an index parameter in our DataFrame

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.','Bland.']},
            index =['Product A', 'Product B'])


# We can create a Series (it is a list).

pd.Series([1, 2, 3, 4, 5])


# We can assign an index parameter to the Series:
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

# A DataFrame can be seen as a bunch of Series.


# # Reading common file formats
# read_csv() function for reading the Data into a DataFrame.


wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")

# shape attribute to check how large the DataFrame is:

wine_reviews.shape


# head() command grabs the first five rows:

wine_reviews.head()

# We want pandas use the in-built index, so we have to specify index_col

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
wine_reviews.head()


# We want to read an excel file: we have to specify the name of the sheet of interest.

wic = pd.read_excel("WICAgencies2013ytd.xls", sheet_name='Total Women')
wic.head()

wic_pregnant = pd.read_excel("WICAgencies2013ytd.xls", sheet_name='Pregnant Women Participating')
wic_pregnant.head()

# We want to save this `DataFrame` to disc as a `csv` file with the name `cows_and_goats.csv`.
q6_df = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
q6_df

q6_df.to_csv("cows_and_goats.csv")

