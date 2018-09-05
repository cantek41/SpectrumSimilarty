#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 04:34:53 2018

@author: can
"""
import pandas as pd
import numpy as np
import SimilartyLib as sim
#
#from sklearn.decomposition import PCA
#from sklearn import preprocessing


import createGraph as cG
import graph_tool.all as gt

indElement= ["al2","cu2","fe2","Mg2","teb","Ti2"]#,"Kk","Lit","Naa","Nn","Oo","Ti"]
coll=["cos","euclidean","manhattan","minkowski","jaccard","graph"]
result=pd.DataFrame(index=indElement,columns=coll)

measures = sim.Similarity()

guess=pd.read_excel("olcumler/al2.xlsx",header=None, names=["Wavelength","Sum"],skiprows=4)#sep=",",index_col=0,usecols=["Wavelength","Sum"])

start=100

guess=guess.query('Sum > '+str(start))
guess=guess.sort_values('Sum', ascending=False)
#guess=guess.iloc[0:300,:]
g=guess['Wavelength'].values
#ssss= source.query('index < 222 | index > 444')

for el in indElement:
    source=pd.read_excel("datalar/"+el+".xlsx",header=None, names=["Wavelength","Sum"],skiprows=4)#,sep=",",index_col=0,usecols=["Wavelength","Sum"])
#    source.index.min()
#    start=max(float(source.index.min()),guess.index.min())
#    end=min(float(source.index.max()),guess.index.max())
    
#    source=source.query('index > '+str(start)+' and index < '+str(end))
#    guess=guess.query('index > '+str(start)+' and index < '+str(end))
#    source= source[start:end]    
#    guess=guess[start:end]
    
    source=source.query('Sum > '+str(start))
    source=source.sort_values('Sum', ascending=False)
#    source=source.iloc[0:300,:]
   
    s=source['Wavelength'].values
  
    if len(s) ==0:
        continue    
    
    grapg_g = cG.create(guess)    
    grapg_s = cG.create(source)            
    graph_sim=gt.similarity(grapg_g,grapg_s)
    
    result.xs(el)['graph']=graph_sim  
#    print(el, "benzerlik oranı  \t%",graph_sim*100)

    result.xs(el)['cos']=measures.cosine_similarity(s,g)   
    
    result.xs(el)['jaccard']=measures.jaccard_similarity(s,g)    
    
    result.xs(el)['euclidean']=measures.euclidean_distance(s,g)
    
        
    result.xs(el)['manhattan']=measures.manhattan_distance(s,g)
    
    
    result.xs(el)['minkowski']=measures.minkowski_distance(s,g,3)

print (result)