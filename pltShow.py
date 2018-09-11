#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 09:07:44 2018

@author: can
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap

labels = ["Al","Cu","Fe","Mg","Ti"]
xlabels = ["al","cu","fe","Mg","Ti"]
xnlabels = ["0","1","2","3","4"]
data_sets = []


#from sklearn.neighbors import KNeighborsClassifier
#knn=KNeighborsClassifier(n_neighbors=10,leaf_size=1,
#                         metric='chebyshev',p=2
#                         ,algorithm='auto',weights='distance')
#knn.fit(x_train,y_train)



ddd=pd.DataFrame(columns=list("ABC"))
#fig = plt.figure()
#ax = fig.add_subplot(111)#, polar=True)
index=0
for el in xlabels:
    x_data=pd.read_excel("datalar/"+el+"2.xlsx",header=None, names=["Wavelength","Sum"],skiprows=4)
#    h=x_data.T
    t_test=x_data.query("Sum>1000")
    t_test=t_test.sort_values('Sum', ascending=False)
    t_test=t_test.iloc[0:10,:]
    x=t_test.iloc[:,0:1]
    y=t_test.iloc[:,1:2]/100
#    ddd.append(x,y,el)
    dfA = pd.DataFrame(data=x.values,columns=list("A"))
    dfB = pd.DataFrame(data=y.values,columns=list("B"))
    dfC = pd.DataFrame(columns=list("C"))
    for i in range(10):
        dfC = dfC.append({'C': index}, ignore_index=True)
    dfFull=pd.concat([dfA,dfB,dfC],axis=1)
    ddd=ddd.append(dfFull)
#    data_sets.append(t_test)
#    area = 2 * t_test.iloc[:,1:2]**(1/3)
#    ax.scatter(x,y, s = area,cmap='hsv', alpha=0.75)
    index =index+1

from sklearn import neighbors
#
#X = iris.data[:, :2]
#y = iris.target
n_neighbors = 15

X=ddd.iloc[:,0:2].values
y=ddd.iloc[:,-1:]
y=y.astype('int')
h = 10 # step size in the mesh

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF','#FF55AA','#55AAAA'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF','#FF00AA','#55FFAA'])

weights ='uniform'#, 'distance']:
# we create an instance of Neighbours Classifier and fit the data.
#from sklearn.cross_validation import train_test_split
#x_train, x_test, y_train, y_test = train_test_split(X,y, 
#                                                    test_size=0.33, random_state=42)
#from sklearn.linear_model import LogisticRegression
#lr=LogisticRegression()
#lr.fit(x_train,y_train)
#y_pred=lr.predict(x_test)

#from sklearn.neighbors import KNeighborsClassifier
#clf=KNeighborsClassifier(n_neighbors=10,
#                         metric='chebyshev',weights='distance')
#from sklearn.svm import SVC
#clf=SVC(kernel='linear',probability=False,degree=5, random_state=None, shrinking=True,
#    tol=0.001)
from sklearn.linear_model import LogisticRegression
clf=LogisticRegression()
#clf.fit(x_train,y_train)
#clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
clf.fit(X, y)

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, x_max]x[y_min, y_max].
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)

plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
            edgecolor='k', s=30)
#plt.legend(xnlabels)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("Classification LogisticRegression")

plt.show()
