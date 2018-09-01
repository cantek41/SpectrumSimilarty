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
from sklearn import preprocessing


import createGraph as cG
import graph_tool.all as gt

indElement= ["All","Bb","Caa","Cc","Cll","Ff","Kk","Lit","Naa","Nn","Oo","Ti"]
coll=["cos","euclidean","manhattan","minkowski","jaccard","graph"]
result=pd.DataFrame(index=indElement,columns=coll)

measures = sim.Similarity()

guess=pd.read_csv("Numune/Al.csv",sep=",",index_col=0,usecols=["Wavelength","Sum"])



for el in indElement:
    source=pd.read_csv("data/"+el+".csv",sep=",",index_col=0,usecols=["Wavelength","Sum"])
    source.index.min()
    start=max(source.index.min(),guess.index.min())
    end=min(source.index.max(),guess.index.max())
    source=source[start:end]
    guess=guess[start:end]
    s=source['Sum'].values
    g=guess['Sum'].values
    
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