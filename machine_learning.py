
# # Supervised learning example: Linear Regression
import seaborn as sns

# Ronald Fisher DB made in 1936
iris = sns.load_dataset('iris')

iris.head()

# pairplot() allows to visualize multidimensional relationships among thr samples:

get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns; sns.set()
sns.pairplot(iris, hue='species', size=2.5)

X_iris = iris.drop('species',axis=1)  # you can drop a column of the DB
X_iris.shape

X_iris.head(10)

y_iris = iris['species'] # 
y_iris.shape

y_iris.head()

type(y_iris)

import matplotlib.pyplot as plt
import numpy as np

# It fixes a seed
rng = np.random.RandomState(42)

# randn() returns a sample from the "standard normal" distribution.
x = 10 * rng.rand(50)

y = 2*x -1 + rng.randn(50)   # TARGET variable

plt.scatter(x,y);

# Let us compute a simple linear regression model:

from sklearn.linear_model import LinearRegression

# We want to fit the intercept using the fit_intercept hyperparameter:
model = LinearRegression(fit_intercept=True)
model

X = x[:, np.newaxis]  # 2d features matrix
X.shape

# Fit the model (Linear Regression) to our data with fit method:
model.fit(X,y)

model.coef_   # slope

model.intercept_  # intercept

xfit = np.linspace(-1,11) # 50 points on x axis

len(xfit)

Xfit = xfit[:,np.newaxis] # 2D feature matrix

yfit = model.predict(Xfit) # feed the matrix into the model

plt.scatter(x,y)     # row data
plt.plot(xfit,yfit)  # model fit


# # IRIS Classification
# We split the data into training ad testing set:

from sklearn.cross_validation import train_test_split

Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris, random_state=1)

# Gaussian naive Bayes assumes each class is drawn from an axis-aligned Gaussian distribution

from sklearn.naive_bayes import GaussianNB   # 1. choose model class
model = GaussianNB()                         # 2. instantiate model
model.fit(Xtrain, ytrain)                    # 3. fit the model to data
y_model = model.predict(Xtest)               # 4. predict on new data

# We can see the fraction of predicted labels through accuracy_score

from sklearn.metrics import accuracy_score
accuracy_score(ytest, y_model)

The accuracy 97% is good even with naive classification.
# # Unsupervised learning example: Iris dimensionality

# The Iris data is 4 dimensional. We can reduce the dimensionality with 
# PCA (Principal Component Analysis):

from sklearn.decomposition import PCA    # 1. Choose the model class
model = PCA(n_components=2)              # 2. Instantiate the model with hyperparameters 
model.fit(X_iris)                        # 3. Fit the model to data (y is not specified)
X_2D = model.transform(X_iris)           # 4. Transform the data to two dimensions

# In the 2D representation, the species are well separated. 

iris['PCA1'] = X_2D[:,0]
iris['PCA2'] = X_2D[:,1]
sns.lmplot("PCA1","PCA2",hue='species',data=iris,fit_reg=False)


# # Unsupervised learning: Iris clustering

# Let us apply clusteringto the Iris data. 

from sklearn.mixture import GMM                      # 1. Choose the model class
model = GMM(n_components=3, covariance_type='full')  # 2. Instantiate the model with hyperparameters
model.fit(X_iris)                                    # 3. Fit to data (y is not specified)
y_gmm = model.predict(X_iris)                        # 4. Determine cluster labels

# Let us add the cluster label to the Iris Dataframe 

iris['cluster'] = y_gmm

# Let us Seaborn to plot the results:

sns.lmplot("PCA1","PCA2", data=iris, hue='species', col='cluster', fit_reg=False)

We can see that splitting the data by cluster number it is possible to separate the flowers with a clustering algorithm.
