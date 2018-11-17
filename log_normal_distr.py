
# coding: utf-8

# # Generate random numbers from a normal distribution:

import scipy as sp
x = sp.random.standard_normal(size=10)
print(x)
y = sp.random.normal(0,1,10) # mean, standard deviation, number of random numbers.
print(y)
help(sp.random.normal)

import scipy as sp
import scipy.stats as stats
import matplotlib.pyplot as plt
x = sp.arange(-4,4,0.01)
y = stats.norm.pdf(x)   # Probability density function
plt.plot(x,y)
plt.title("A standard normal distribution")
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# # Generating random numbers with a seed

import scipy as sp
sp.random.seed(12345)   # 12345 is a seed
x = sp.random.normal(0,1,20)
print (x[0:5])


# # Random numbers from a normal distribution

import scipy as sp
sp.random.seed(12345)
mean = 0.05     # Now I choose a mean of 0.05
std = 0.1       # and a standard deviation of 0.1
n = 50
x = sp.random.normal(mean,std,n)
print(x[0:5])


# # Histogram for a normal distribution

import scipy as sp
import matplotlib.pyplot as plt
sp.random.seed(12345)
mean = 0.1
std = 0.2
n = 1000
x = sp.random.normal(mean,std,n)
plt.hist(x, 15, density=True)
plt.title("Histogram for random numbers drawn from a normal distribution")
plt.annotate("mean="+str(mean),xy=(0.6,1.5))   # legenda
plt.annotate("std="+str(std),xy=(0.6,1.4))
plt.show()


# # Graphical presentation of a lognormal distribution

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.001,3,200)
mu = 0
sigma0 = [0.25,0.5,1]      # 3 sigma 
color = ['blue','red','green']  # colori dei grafici delle distribuzioni
target = [(1.2,1.3),(1.7,0.4),(0.18,0.7)]  # punti finali dei vettori
start = [(1.8,1.4),(1.9,0.6),(0.18,1.6)]  # punti iniziali dei vettori

for i in sp.arange(len(sigma0)):
    sigma=sigma0[i]
    y=1/(x*sigma*np.sqrt(2*np.pi))*np.exp( -(np.log(x)-mu)**2/(2*sigma**2) )
    plt.annotate('mu='+str(mu)+', sigma='+str(sigma),xy=target[i], xytext=start[i], # xy inizio del vettore 
                 arrowprops=dict(facecolor=color[i],shrink=0.01),)      # xytext fine del vettore 
    plt.plot(x,y,color[i])
    plt.title('Lognormal distribution')
    plt.xlabel('x')
    plt.ylabel('lognormal density distribution')

plt.show()

