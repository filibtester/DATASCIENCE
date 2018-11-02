
# coding: utf-8

# # Indexing, selecting, assigning reference

# In[1]:


import pandas as pd
import seaborn as sns

get_ipython().run_line_magic('run', "'renaming_and_combining.py'  # to run a python file inside the notebook")


# In[2]:


reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0) # read the DataBase


# In[3]:


pd.set_option("display.max_rows",5)


# In[4]:


# Look at an overview of your data:

reviews.head()


# In[5]:


# We have to know how to slice and dice a dataset.


# In[6]:


reviews.shape  # to get rows and columns of the DataSet.


# # How to access a column of a DataSet

# In[7]:


reviews.country  # to access the column country (attribute of an object)


# In[8]:


reviews['country']  # we can access the value of a dict with the indexing operator [] 


# In[11]:


# the indexing operator can handle reserved characters like space.


# In[12]:


# We can consider pandas Series as dictionaries and use [] operator.

reviews['country'][1]


# In[13]:


# I want to access the second column:

reviews['description']


# In[14]:


# I want to access the first value from the description column of reviews:

reviews['description'][0]


# In[48]:


# Select the 'points' column for the last 1000 wines.

reviews.points[-1000:]


# # Index-based selection

# In[15]:


# Pandas has its own operators for accessing data: loc and iloc 


# In[16]:


# To select the first row of data in this DataFrame:

reviews.iloc[0]


# In[9]:


# To select a column with iloc:

reviews.iloc[:,0]   # all the rows, first column


# In[10]:


# To select the 'country' column from just the first, second and third row:

reviews.iloc[:3,0]   # 3 is excluded


# In[11]:


# To select just the second and third entries:

reviews.iloc[1:3,0]


# In[12]:


# It is possible to pass a list:

reviews.iloc[[0,1,2],0]


# In[13]:


# We want to select the records with the 1,2,3,5,8 row index positions.
# We can do it passing a list to iloc.

reviews.iloc[[1,2,3,5,8],:]   


# In[14]:


# Select the 'country', 'province', 'region_1' and 'region_2' columns
# with the 0,1,10, and 100 index positions

# We can use loc but not iloc.
reviews.loc[[0,1,10,100],['country','province','region_1','region_2']]


# In[15]:


# Select the country and variety columns of the first 100 records.

reviews.loc[:99,['country','variety']]


# In[16]:


# Select the country and variety columns of the first 100 records.

reviews.loc[:99,['country','variety']]


# In[17]:


# Negative numbers can be used in selection. 

reviews.iloc[-5:]  # last five elements of DataSet.


# # Label based selection

# In[18]:


reviews.loc[0,'country']


# In[19]:


# loc uses the information in the indices :

reviews.loc[:,['taster_name', 'taster_twitter_handle', 'points']]


# In[20]:


# iloc uses STDLIB scheme, where first element is included and last escluded.
# loc is indexes inclusively ----> 1 element more.


# # Manipulating the index

# In[21]:


reviews.set_index("title")     # we set index to title field


# In[27]:


# Performing a set_index is useful if you come up with an index for the dataset better 
# than the current one.


# # Conditional Selection

# In[22]:


# We want to ask questions based on conditions. 


# In[23]:


# Let's ask if the wine is italian or not.


# In[25]:


reviews['country'] == 'France'


# In[27]:


# The results can be used inside of 'loc' to select the relevant data.
# to select only france wines.
reviews.loc[reviews['country'] == 'France']


# In[28]:


# ~22 thousands wines are from France.


# In[29]:


# ~20000 wines are Italian out of ~130000 wines. (15%)


# In[30]:


# We want to know which ones are better than average. We can accept wines with more than
# 90 points.


# In[32]:


reviews.loc[ (reviews['country'] == 'France') & (reviews['points'] >= 90)]


# In[46]:


# There are 9 France thousands wines with more than 90 points.


# In[47]:


# & --> AND   ampersand
# | --> OR    pipe


# In[50]:


# We want an Italian wine OR a wine rated above the average.


# In[51]:


reviews.loc[ (reviews['country'] == 'Italy') | (reviews['points'] >= 90)]


# In[52]:


# There are conditional selectors in PANDAS: isin


# In[53]:


# Suppose we want wines from Italy or from France:


# In[54]:


reviews.loc[reviews['country'].isin(['Italy','France'])]


# In[55]:


reviews.loc[reviews.country.isin(['Italy','France'])]  # other way 


# In[56]:


# the second selector is ISNULL / NOTNULL


# In[57]:


# We can filter out wines lacking a price tag in the dataset:
reviews.loc[reviews.price.notnull()]


# In[58]:


# Select wines whose region_2 is not NaN. 

reviews.loc[reviews.region_2.notnull()]


# In[59]:


# We can select wines lacking a price tag in the dataset:
reviews.loc[reviews.price.isnull()]


# # Assigning Data

# In[60]:


# We can assign a constant value:

reviews['critic'] = 'everyone'
reviews['critic']


# In[61]:


reviews['index_backwards'] = range(len(reviews), 0, -1)   # new column 
reviews['index_backwards']


# In[62]:


reviews


# In[63]:


# Who produces more above-averagely good wines, France or Italy? Select the `country` column, 
# but only when said `country` is one of those two options, _and_ the `points` column is greater than or equal to 90.

reviews.country.loc [((reviews['country'] == 'Italy') |  (reviews['country'] == 'France')) & (reviews['points'] >= 90)]

