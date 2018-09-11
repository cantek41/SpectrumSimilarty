#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 04:34:53 2018

@author: can
"""
import pandas as pd
import numpy as np
import SimilartyLib as sim
from sklearn.decomposition import PCA
import createGraphPCAdata as cG
import graph_tool.all as gt
import matplotlib.pyplot as plt

indElement= ["al2","cu2","fe2","Mg2","Ti2"]#,"Kk","Lit","Naa","Nn","Oo","Ti"]
coll=["cos","euclidean","minkowski","graph"]
result=pd.DataFrame(index=indElement,columns=coll)

measures = sim.Similarity()

guess=pd.read_excel("olcumler/Numune/als2-1.xlsx",header=None, names=["Wavelength","Sum"],skiprows=4)#sep=",",index_col=0,usecols=["Wavelength","Sum"])

pca = PCA(n_components=1)
pca.fit(guess)
g=pca.transform(guess)
g=g[:,0]
#
#print("original shape:   ", guess.shape)
#print("transformed shape:", g.shape)

#plt.plot(g, 'ro')
#plt.show()

#X_new = pca.inverse_transform(g)
#plt.plot(guess,"r", alpha=0.5)
#plt.plot(X_new,"b", alpha=0.8)
#plt.axis('equal');

#plt.plot(pca.explained_variance_, linewidth=2)
#plt.show()


gPCA=pd.DataFrame(data=g,columns=['PCA'])

for el in indElement:
    source=pd.read_excel("datalar/"+el+".xlsx",header=None, names=["Wavelength","Sum"],skiprows=4)#,sep=",",index_col=0,usecols=["Wavelength","Sum"])

    s=pca.transform(source)
#    x=pca.score_samples(s)
#    print(x)
    s=s[:,0]
    if len(s) ==0:
        continue
    
    sPCA=pd.DataFrame(data=s,columns=['PCA'])
    
   
    grapg_g = cG.create(gPCA)    
    grapg_s = cG.create(sPCA)            
    graph_sim=gt.similarity(grapg_g,grapg_s)
    
    result.xs(el)['graph']=graph_sim  
#    print(el, "benzerlik oranı  \t%",graph_sim*100)

    result.xs(el)['cos']=measures.cosine_similarity(s,g)   
    
#    result.xs(el)['jaccard']=measures.jaccard_similarity(s,g)    
    
    result.xs(el)['euclidean']=measures.euclidean_distance(s,g)
    
        
#    result.xs(el)['manhattan']=measures.manhattan_distance(s,g)
    
    
    result.xs(el)['minkowski']=measures.minkowski_distance(s,g,3)

print (result)