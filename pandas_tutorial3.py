
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[9]:


reviews = pd.read_csv("winemag-data-130k-v2.csv")
reviews.head()


# # Summary Functions

# In[10]:


reviews.points.describe()   # applied to float 


# In[11]:


reviews.taster_name.describe() # applied to string


# In[12]:


reviews.points.mean()


# In[13]:


reviews.taster_name.unique()


# In[14]:


reviews


# In[15]:


reviews.taster_name.value_counts()


# # Maps

# In[17]:


review_points_mean = reviews.points.mean()
print(review_points_mean)


# In[18]:


reviews.points.map(lambda p: p - review_points_mean)


# In[29]:


def remean_points(srs):
    srs.points = srs.points - review_points_mean
    return srs

reviews.apply(remean_points, axis='columns')   # apply function


# In[31]:


review_points_mean = reviews.points.mean()
reviews.points - review_points_mean


# In[35]:


reviews.country  + " - " + reviews.region_1

