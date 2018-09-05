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
from sklearn.preprocessing import StandardScaler, LabelEncoder

x=pd.read_excel("datalar/dataSet.xlsx",header=None)


x_data=x.iloc[1:,1:]
y_target=x.iloc[1:,0:1]

#lb=LabelEncoder()
#y_target=lb.fit_transform(y_target.ravel())




x_train, x_test, y_train, y_test = train_test_split(x_data,y_target, 
                                                    test_size=0.25, random_state=42)



#sc=StandardScaler()
#X_train=sc.fit_transform(x_train)
#X_test=sc.fit_transform(x_test)
#Y_train=sc.fit_transform(y_train)
#Y_test=sc.fit_transform(y_test)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)


test=pd.read_excel("olcumler/al2.xlsx",header=None, names=["Wavelength","Sum"],skiprows=4)
h=test.T
t_test=h.iloc[1:,:].values

y_pred=lr.predict(t_test)


#svc=SVC(kernel='sigmoid')
#svc.fit(x_train,y_train)
#y_pred=svc.predict(x_test)
#cm=confusion_matrix(y_test,y_pred)
#print(cm)
#x=pd.read_excel("datalar/dataSet.xlsx",header=None, names=["Wavelength","Sum"],skiprows=4)#sep=",",index_col=0,usecols=["Wavelength","Sum"])
#pca = PCA(n_components=1)
#g=pca.fit_transform(guess)
#g=g[:,0]
#
#gPCA=pd.DataFrame(data=g,columns=['PCA'])

