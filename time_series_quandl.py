
# coding: utf-8

import pandas as pd
import os
import quandl
quandl.ApiConfig.api_key = "VCJv6wihwixyRmsziU1s"
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data1 = quandl.get("EIA/PET_RWTC_D")
data1.head()

plt.plot(data1.index,data['Value'])
plt.title('EIA/PET_RWTC_D')
plt.ylabel('Price($)')
plt.show()

# You can change format and get the same data in a NumPy array:
data1 = quandl.get("EIA/PET_RWTC_D", returns="numpy")

print(data1)

# You can make a filtered time-series call
data2 = quandl.get("FRED/GDP", start_date="2001-12-31", end_date="2005-12-31")

data2.head()

plt.plot(data2.index,data2['Value'])
plt.title('FRED/GDP')
plt.ylabel('Price($)')
plt.show()

# To request specific columns:
data3 = quandl.get(["NSE/OIL.1","WIKI/AAPL.4"])
data3.head()

# To request the last 5 rows:
data4 = quandl.get("WIKI/AAPL", rows=5)
print(data4)

# To change the sampling frequency:
data5 = quandl.get("EIA/PET_RWTC_D", collapse="monthly")
data5.head()

# To perform elementary calculations on the data:
data6 = quandl.get("FRED/GDP", transformation="rdiff")
data6.head()

dow_jones = quandl.get("BCB/UDJIAD1")

dow_jones.head()

dow_jones3 = quandl.get("BCB/7809")

plt.plot(dow_jones3.index,dow_jones3['Value'])
plt.title('Dow Jones Industrial Average 2000-2018')
plt.ylabel('Price($)')
plt.show()

# You can make a filtered time-series call '90
dow_jones2 = quandl.get("BCB/UDJIAD1", start_date="1991-01-01", end_date="2000-12-31")

plt.plot(dow_jones2.index,dow_jones2['Value'])
plt.title('Dow Jones Industrial Average 1991-2000')
plt.ylabel('Price($)')
plt.show()

# You can make a filtered time-series call 2000
dow_jones1 = quandl.get("BCB/UDJIAD1", start_date="2001-01-01", end_date="2010-12-31")

plt.plot(dow_jones1.index,dow_jones1['Value'])
plt.title('Dow Jones Industrial Average 2001-2010')
plt.ylabel('Price($)')
plt.show()

# You can make a filtered time-series call '90
dow_jones6 = quandl.get("BCB/7809", start_date="2001-01-01", end_date="2010-12-31")

plt.plot(dow_jones6.index,dow_jones6['Value'])
plt.title('Dow Jones Industrial Average 2001 - 2010')
plt.ylabel('Price($)')
plt.show()

# You can make a filtered time-series call
dow_jones3 = quandl.get("BCB/UDJIAD1", start_date="2011-01-01", end_date="2015-12-31")

plt.plot(dow_jones3.index,dow_jones3['Value'])
plt.title('Dow Jones Industrial Average 2011 - 2015')
plt.ylabel('Price($)')
plt.show()

# You can make a filtered time-series call '90
dow_jones7 = quandl.get("BCB/7809", start_date="2011-01-01", end_date="2015-12-31")

plt.plot(dow_jones7.index,dow_jones7['Value'])
plt.title('Dow Jones Industrial Average 2011 - 2015')
plt.ylabel('Price($)')
plt.show()

# You can make a filtered time-series call
dow_jones8 = quandl.get("BCB/7809", start_date="2016-01-01", end_date="2017-12-31")

dow_jones8.head()

fig, ax = plt.subplots(figsize=(15,7))
dow_jones8.plot(ax=ax)
plt.title('Dow Jones Industrial Average 2016-2017')
plt.ylabel('Price($)')
plt.show()

# You can make a filtered time-series call
dow_jones9= quandl.get("BCB/7809", start_date="2018-01-01", end_date="2018-12-31")

fig, ax = plt.subplots(figsize=(15,7))
dow_jones9.plot(ax=ax)
plt.title('Dow Jones Industrial Average 2018')
plt.ylabel('Price($)')
plt.show()

# You can make a filtered time-series call
dow_jones10= quandl.get("BCB/7809", start_date="2018-01-01", end_date="2018-06-30")

fig, ax = plt.subplots(figsize=(15,7))
dow_jones10.plot(ax=ax)
plt.title('Dow Jones Industrial Average 2018 - 1st Semester')
plt.ylabel('Price($)')
plt.show()

# You can make a filtered time-series call
dow_jones11= quandl.get("BCB/7809", start_date="2018-07-01", end_date="2018-11-30")

fig, ax = plt.subplots(figsize=(15,7))
dow_jones11.plot(ax=ax)
plt.title('Dow Jones Industrial Average 2018 - 2nd Semester')
plt.ylabel('Price($)')
plt.show()

# You can make a filtered time-series call
dow_jones12= quandl.get("BCB/7809", start_date="2018-10-01", end_date="2018-11-30")

dow_jones12.head()

fig, ax = plt.subplots(figsize=(15,7))
dow_jones12.plot(ax=ax)
plt.title('Dow Jones Industrial Average 2018 - October November 2018')
plt.ylabel('Price($)')
plt.show()

# You can make a filtered time-series call
dow_jones13 = quandl.get("BCB/7809", start_date="2018-11-01", end_date="2018-11-30")

fig, ax = plt.subplots(figsize=(15,7))
dow_jones13.plot(ax=ax)
plt.title('Dow Jones Industrial Average 2018 - October November 2018')
plt.ylabel('Price($)')
plt.show()

plt.plot(dow_jones.index,dow_jones['Value'])
plt.title('Dow Jones Industrial Average')
plt.ylabel('Price($)')
plt.show()

