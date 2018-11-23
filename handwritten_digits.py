
# coding: utf-8

# How can we locate and identify characters in an image?
from sklearn.datasets import load_digits
digits = load_digits()
digits.images.shape

# It is a 3d array: 1797 samples, each consists of 8x8 grid of pixels. Let us visualize them.
import matplotlib.pyplot as plt
fig, axes = plt.subplots(10,10, figsize=(8,8),
                        subplot_kw={'xticks':[],'yticks':[]},
                        gridspec_kw=dict(hspace=0.1,wspace=0.1))

for i, ax in enumerate(axes.flat):       # it is an iterator
    ax.imshow(digits.images[i], cmap='binary', interpolation='nearest') # Display an image, i.e. data on a 2D regular raster.
    ax.text(0.05,0.05,str(digits.target[i]),
           transform=ax.transAxes, color='green')

# We need a 2D representation (n_samples, n_features). We can treat each pixel in the image as a feature.

X = digits.data   # 2D array (n_samples, n_features)
y = digits.target # array which gives the label for each digit

len(X)

X.shape

type(X)

len(y)

y.shape

type(y)

# We have to reduce the dimensionality of the problem from 64 to 2. We can do this using an unsupervised method:
# Isomap algorithm. 

from sklearn.manifold import Isomap           # 1. Choose the model
iso = Isomap(n_components=2)                  # 2. Instantiate the model with hyperparameters 
iso.fit(digits.data)                          # 3. Fit to data. 
data_projected = iso.transform(digits.data)   # 4. Transform the data
data_projected.shape

plt.scatter(data_projected[:,0],data_projected[:,1], c=digits.target,
           edgecolor='none',alpha=0.5,
           cmap=plt.cm.Spectral)
plt.colorbar(label='digit label', ticks=range(10))
plt.clim(-0.5,9.5)


# The group of digits appear to be well separated in the parameter space. Therefore, a supervised algorithm should perform well. 

# # Supervised Learning

from sklearn.cross_validation import train_test_split

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)

from sklearn.naive_bayes import GaussianNB  # 1. Choose the model
model = GaussianNB()                        # 2. Instantiate the model
model.fit(Xtrain,ytrain)                    # 3. Fit to data
y_model = model.predict(Xtest)              # 4. Predict our model

from sklearn.metrics import accuracy_score
accuracy_score(ytest,y_model)

# # Confusion Matrix

from sklearn.metrics import confusion_matrix

mat = confusion_matrix(ytest,y_model)

import seaborn as sns

sns.heatmap(mat, square=True, annot=True, cbar=False)
plt.xlabel('predicted value')
plt.ylabel('true value')


# A large number of 3 are missclassified as either ones or eights.

fig, axes = plt.subplots(10, 10, figsize=(8, 8),
subplot_kw={'xticks':[], 'yticks':[]},
gridspec_kw=dict(hspace=0.1, wspace=0.1))

for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap='binary', interpolation='nearest')
    ax.text(0.05, 0.05, str(y_model[i]),
        transform=ax.transAxes,
        color='green' if (ytest[i] == y_model[i]) else 'red')

