#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 04:34:53 2018

@author: can
"""
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import PolynomialFeatures, LabelEncoder
import os

coll=["LR","SVM","KNN"]

indElement=os.listdir("olcumler/Numune")
result=pd.DataFrame(index=indElement,columns=coll)

x=pd.read_excel("datalar/dataSet.xlsx",header=None)


x_data=x.iloc[1:,1:]
y_target=x.iloc[1:,0:1]
y_target=y_target.reset_index(drop=True)
lb=LabelEncoder()
y_target_code=lb.fit_transform(y_target)
#
dd=pd.DataFrame(data=y_target_code,columns=["code"])
ff=pd.DataFrame(data=y_target.values,columns=["name"])
son=pd.concat([dd,ff],axis=1)
x_train, x_test, y_train, y_test = train_test_split(x_data,y_target_code, 
                                                    test_size=0.33, random_state=42)

# create a mesh to plot in
h = .02  # step size in the mesh
x_min, x_max = x.iloc[0, :].min() - 1, x.iloc[0, :].max() + 1
y_min, y_max = 0, 6000
xx, yy = np.meshgrid(np.arange(x_min, x_max),
                     np.arange(y_min, y_max))



#pca = PCA(n_components=2)
#pca.fit(x_data)
#principalComponents=pca.transform(x_data)
#
#principalDf = pd.DataFrame(data = principalComponents
#             , columns = ['PCA 1', 'PCA 2'])
#finalDf = pd.concat([principalDf, ff], axis = 1)

#LogisticRegression 
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
#
#x_train=pca.transform(x_train)
##y_train=pca.transform(y_train)
#x_test=pca.transform(x_test)
#y_test=pca.transform(y_test)

lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)
cm=confusion_matrix(y_pred,y_test)
print("LR")
print(cm)

##SVM 
svc=SVC(kernel='linear',probability=False,degree=5, random_state=None, shrinking=True,
    tol=0.001)
svc.fit(x_train,y_train)

y_pred=svc.predict(x_test)
cm=confusion_matrix(y_pred,y_test)
print("SVM")
print(cm)

#print(svc.coef_[0])


import matplotlib.pyplot as plt
#
#fig = plt.figure()
#ax = fig.add_subplot(1,1,1) 
#ax.set_xlabel('PCA 1', fontsize = 15)
#ax.set_ylabel('PCA 2', fontsize = 15)
#ax.set_title('2 component PCA', fontsize = 10)
##targets = y_target.iloc[:,0]
#targets = ["Al","Cu","Fe","Mg","Ti"]
##colors = ['r', 'g', 'b','y']
##for target, color in zip(targets,colors):
#for target in targets:
#    indicesToKeep = finalDf['name'] == target
##    print("dd",indicesToKeep)
#    ax.scatter(finalDf.loc[indicesToKeep, 'PCA 1']
#               , finalDf.loc[indicesToKeep, 'PCA 2']
##               , c = color
#               , s = 50)
#ax.legend(targets)
#ax.grid()



#figl = plt.figure()
#ax = figl.add_subplot(1,1,1) 
#ax.set_xlabel('PCA 1', fontsize = 15)
#ax.set_ylabel('PCA 2', fontsize = 15)
#ax.set_title('2 component PCA', fontsize = 10)
##targets = y_target.iloc[:,0]
#targets = ["Al","Cu","Fe","Mg","Ti"]
##colors = ['r', 'g', 'b','y']
##for target, color in zip(targets,colors):
#X1,X2=np.meshgrid(np.arange(0,1000),
#                  np.arange(0,6000))
#ax.contourf(X1, X2, x_data)#, cmap=plt.cm.Paired, alpha=0.8)
#for target in targets:
#    indicesToKeep = finalDf['name'] == target
##    print("dd",indicesToKeep)
#    ax.scatter(finalDf.loc[indicesToKeep, 'PCA 1']
#               , finalDf.loc[indicesToKeep, 'PCA 2']
##               , c = color
#               , s = 50)
#ax.legend(targets)
#ax.grid()

#
#from matplotlib.colors import ListedColormap
#x_set, y_set= x_train, y_train
#X1,X2=np.meshgrid(np.arange(0,6000),
#                  np.arange(0,6000))
#
#plt.contourf(X1, X2, y_pred, cmap=plt.cm.Paired, alpha=0.8)
#plt.scatter(x_train,y_train)
#plt.legend()
#plt.show()

#plt.contourf(xx, yy, y_pred, cmap=plt.cm.Paired, alpha=0.8)
#plt.scatter(x_train.iloc[:, 0], x_train.iloc[:, 1], c=y_target,
#            cmap=plt.cm.Paired)
#plt.xlabel(X.columns[0], size=14)
#plt.ylabel(X.columns[1], size=14)
#plt.title('SVM Decision Region Boundary', size=16)

##KNN
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=10,leaf_size=1,
                         metric='chebyshev',p=2
                         ,algorithm='auto',weights='distance')
knn.fit(x_train,y_train)



y_pred=knn.predict(x_test)
cm=confusion_matrix(y_pred,y_test)
print("KNN")
print(cm)

for el in indElement:
    test=pd.read_excel("olcumler/Numune/"+el,header=None, names=["Wavelength","Sum"],skiprows=4)
    h=test.T
    t_test=h.iloc[1:,:].values
    y_pred=lr.predict(t_test)
    result.xs(el)['LR']=getStringCode(y_pred[0])
    
    y_pred=svc.predict(t_test)
    result.xs(el)['SVM']=getStringCode(y_pred[0])
    
    
    
    y_pred=knn.predict(t_test)
    result.xs(el)['KNN']=getStringCode(y_pred[0])
    

def getStringCode(code):
    result=son.query("code=="+str(code)).head(1)
    result = result.iloc[:,1].values[0]
    return result
#sc=StandardScaler()
#X_train=sc.fit_transform(x_train)
#X_test=sc.fit_transform(x_test)
#Y_train=sc.fit_transform(y_train)
#Y_test=sc.fit_transform(y_test)


#
#y_pred=lr.predict(x_test)
#cm=confusion_matrix(y_test,y_pred)
#print(cm)
#


#svc=SVC(kernel='linear',probability=False,degree=5, random_state=None, shrinking=True,
#    tol=0.001)
#svc.fit(x_train,y_train)
#y_pred=svc.predict(x_test)
#cm=confusion_matrix(y_test,y_pred)
#print(cm)
#y_pred=svc.predict(t_test)
#print(son.query("code=="+str(y_pred[0])).head(1))

#x=pd.read_excel("datalar/dataSet.xlsx",header=None, names=["Wavelength","Sum"],skiprows=4)#sep=",",index_col=0,usecols=["Wavelength","Sum"])
#pca = PCA(n_components=1)
#g=pca.fit_transform(guess)
#g=g[:,0]
#
#gPCA=pd.DataFrame(data=g,columns=['PCA'])

