import pandas as pd
from sklearn.decomposition import PCA
import createGraphPCAdata as cG
import graph_tool.all as gt
import matplotlib.pyplot as plt


guess=pd.read_excel("olcumler/Numune/als2-1.xlsx",header=None, names=["Wavelength","Sum"],skiprows=4)#sep=",",index_col=0,usecols=["Wavelength","Sum"])

pca = PCA(n_components=1)
pca.fit(guess)
g=pca.transform(guess)
g=g[:,0]# -*- coding: utf-8 -*-
gPCA=pd.DataFrame(data=g,columns=['PCA'])
grapg_g = cG.create(gPCA) 
pos = gt.sfdp_layout(grapg_g)
#gt.graph_draw(grapg_g, pos=pos, output="cc.pdf")




