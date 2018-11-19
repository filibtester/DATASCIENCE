
# coding: utf-8

# # Random numbers from uniform distribution

import numpy as np
import scipy as sp
sp.random.seed(123345)  
x = sp.random.uniform(low=1,high=100,size=10)
print(x[0:5])

import random
def rollDice():                   # function that gives a number from 1 to 6
    roll = random.randint(1,6)    # Return random integers from low (inclusive) to high (exclusive).
    return roll

i = 1
n = 10
result = []
random.seed(123)
while i < n:
    result.append(rollDice())
    i+=1
print(result)

# # Estimate pi value
# Let us generate n pairs of x and y from a uniform distribution with a range of 0 and 0.5 (radius).
# We estimate the distance d. If d < 0.5 the dart is in the circle, 
# otherwise it is in the square outside the circle

import scipy as sp
n = 1000000
x = sp.random.uniform(low=0,high=1,size = n)
y = sp.random.uniform(low=0,high=1,size = n)
dist = sp.sqrt(x**2+y**2)   # It is an array
in_circle = dist[dist<1]    # It is an array with element less than 1
our_pi = len(in_circle)*4./n
print ('pi=',our_pi)
print('error (%)=', (our_pi-sp.pi)/sp.pi)

len(dist) # same length of number of simulations

len(in_circle)  # length is smaller than n


# # Random numbers from Poisson distribution

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

x = sp.random.poisson(lam=1,size=100)
a = 5. #shape
n = 1000 
s = np.random.power(a,n)   # power function distribution a*x**(a-1.)
count, bins, ignored = plt.hist(s, bins=30)


# In[78]:


x = sp.random.poisson(lam=1,size=100)
a = 5. #shape
n = 1000 
s = np.random.power(a,n)   # power function distribution a*x**(a-1.)
count, bins, ignored = plt.hist(s, bins=30)

x = np.linspace(0,1,100)
y = a*x**(a-1.)
normed_y = n*np.diff(bins)[0]*y  # samples * width of a bin * y (normalization)
plt.title("Poisson distribution")
plt.ylabel("y")
plt.xlabel("x")
plt.plot(x, normed_y)
plt.show()

# # Selecting stocks randomly
# Let us choose 20 stocks from 500 available.

import scipy as sp
n_stocks_available = 500
n_stocks = 20

sp.random.seed(123345)  
x = sp.random.uniform(low=1,high=n_stocks_available,size=n_stocks)
print(x[0:5])

# The array y will contain 20 values taken from random uniform distribution.

y = []
for i in range(n_stocks):
    y.append(int(x[i]))  
print(y)
final = sp.unique(y)   # return the sorted unique elements of the array y
print(final)

# Let us choose n stocks from all the available stocks.
# .pkl is a type of output format from pandas. 

import scipy as sp
import numpy as np
import pandas as pd

n_stocks = 10
x  = pd.read_pickle('yanMonthly.pkl') 
x2 = sp.unique(np.array(x.index))  # select the unique ID of the array of indeces
x3 = x2[x2<'ZZZZ']      # remove all indices starting with ^

len(x)   

len(x.index)

x2

x3

sp.random.seed(1234567)

# list of 10 non stocks (like High Minus Low (HML), risk-free rate (RF) ... )
# with letters. 

nonStocks=['GOLDPRICE','HML','SMB','Mkt_Rf','Rf','Russ3000E_D','US_DEBT',
           'Russ3000E_X','US_GDP2009dollar','US_GDP2013dollar']

type(x3)  # x3 is an array
len(x3)  # x3 contains 109 elements
x4 = list(x3) # Convert an iterable (tuple, string, set, dictionary) to a list.
type(x4)   # type of x4 is list.
len(x4)  # same length of x3.

# I want to remove non stocks from the list

for i in range(len(nonStocks)):
    x4.remove(nonStocks[i])

len(x4) # now we have only 99 elements
k = sp.random.uniform(low=1,high=len(x4),size=n_stocks)  # We want to select 9 stocks 
y,s = [], []
for i in range(n_stocks):
    index = int(k[i])
    y.append(index)
    s.append(x4[index])
    
final = sp.unique(y)
print(final)
print(s)

