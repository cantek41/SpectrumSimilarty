# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

import deepgraph as dg
import graph_tool as gt


def create(vector):     
    
              
#       vector=vector.sort_values('PCA', ascending=False)
       vector=vector.iloc[0:500,:]
#       vector=vector.reset_index()
       g=dg.DeepGraph(vector)
       
#       plt.plot(vector,"b")
#       plt.show()
       
       def x_dist(PCA_s, PCA_t):
           dx = PCA_t - PCA_s
           return dx
#       def x_dist(Sum_s, Sum_t):
#           dx = Sum_t - Sum_s
#           return dx
#       
       g.create_edges(connectors=x_dist)
       
#       print(g)
       
       def x_dist_selector(dx, sources, targets):
           dxa = np.abs(dx)
           sources = sources[dxa <= 100]
           targets = targets[dxa <= 100]
           return sources, targets
       
        
       g.create_edges(connectors=x_dist, selectors=x_dist_selector)
#       print(g)
#       print(g.e)
       
#       g.v.sort_values('Wavelength', inplace=True)
#       print(g.v)
#       g.create_edges_ft(ft_feature=('PCA', 100))
#       print(g)
       
#       def y_dist(Sum_s, Sum_t):
#           dy = Sum_t - Sum_s
#           return dy
#       
#       def y_dist_selector(dy, sources, targets):
#           dya = np.abs(dy)
#           sources = sources[dya <= 100]
#           targets = targets[dya <= 100]
#           return sources, targets
#       
#       g.create_edges_ft(ft_feature=('Wavelength',100),
#                         connectors=y_dist,
#                         selectors=y_dist_selector)

       gtd=g.return_gt_graph()
       return gtd
   
#guess=pd.read_csv("Numune/Ff.csv",sep=",",index_col=0,usecols=["Wavelength","Sum"])
#guess=guess[221.22:576.74]

#ggg=pd.DataFrame(data=guess,index=(xx in range(600)))
#print(create(guess))/
#v = pd.DataFrame({'time': [-3.6,-1.1,1.4,4., 6.3],'x': [-3.,3.,1.,12.,7.]})
#g = dg.DeepGraph(guess)
#print(g.v)
#g.create_edges_ft(ft_feature=('Wavelength', 5))
#print(g.e)