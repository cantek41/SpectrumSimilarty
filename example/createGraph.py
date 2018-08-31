# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

import deepgraph as dg
import graph_tool as gt


def create(name):
#       v=pd.read_csv(name,index_col=0)
#       print(v)

        v=name[:]#[0:300]
#       v=v.sort_values('Sum', ascending=False)[0:300]
#       print(v)
       
#       plt.rcParams['figure.figsize'] = 6, 4
#       pd.options.display.max_rows = 10
#       pd.set_option('expand_frame_repr', False)
#       
#       plt.scatter(v.Wavelength, v.Sum)
       
       g=dg.DeepGraph(v)
       
#       print(g)
       
       def x_dist(Wavelength_s, Wavelength_t):
           dx = Wavelength_t - Wavelength_s
           return dx
       
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
       
       g.v.sort_values('Wavelength', inplace=True)
       
       g.create_edges_ft(ft_feature=('Wavelength', 100))
#       print(g)
       
       def y_dist(Sum_s, Sum_t):
           dy = Sum_t - Sum_s
           return dy
       
       def y_dist_selector(dy, sources, targets):
           dya = np.abs(dy)
           sources = sources[dya <= 1000]
           targets = targets[dya <= 1000]
           return sources, targets
       
       g.create_edges_ft(ft_feature=('Wavelength',100),
                         connectors=y_dist,
                         selectors=y_dist_selector)
#       print(g)
#       print(g.e)
       
#       gtd=g.return_gt_graph()  
#       pos =gt.draw.sfdp_layout(gtd)       
#       weight = gtd.new_edge_property("double")
#       for e in gtd.edges():
#           weight[e] = np.linalg.norm(pos[e.target()].a - pos[e.source()].a)
#           
#       tree = gt.topology.min_spanning_tree(gtd, weights=weight)   
#       
#       gtd = gt.GraphView(gtd, efilt=tree)
#      
#       gt.draw.graph_draw(gtd, pos=pos, edge_color=tree,output=name+".png")
#       
    
#       obj = g.plot_2d('Wavelength', 'Sum', edges=True)
#       obj['ax'].set_xlim(200,600)
       gtd=g.return_gt_graph()
       return gtd
#       
#       print(gtd)

