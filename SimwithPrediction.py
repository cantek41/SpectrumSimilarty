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
y_target=x.iloc[1:,0]

lb=LabelEncoder()
y_target_code=lb.fit_transform(y_target)
#
dd=pd.DataFrame(data=y_target_code,columns=["code"])
ff=pd.DataFrame(data=y_target.values,columns=["name"])
son=pd.concat([dd,ff],axis=1)
x_train, x_test, y_train, y_test = train_test_split(x_data,y_target_code, 
                                                    test_size=0.33, random_state=42)



#LogisticRegression 
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)
#y_pred=lr.predict(x_test)
#cm=confusion_matrix(y_pred,y_test)
#print(cm)

##SVM 
svc=SVC(kernel='linear',probability=False,degree=5, random_state=None, shrinking=True,
    tol=0.001)
svc.fit(x_train,y_train)

#y_pred=svc.predict(x_test)
#cm=confusion_matrix(y_pred,y_test)
#print(cm)

##KNN
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=10,leaf_size=1,
                         metric='chebyshev',p=2
                         ,algorithm='auto',weights='distance')
knn.fit(x_train,y_train)

#y_pred=knn.predict(x_test)
#cm=confusion_matrix(y_pred,y_test)
#print(cm)

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

