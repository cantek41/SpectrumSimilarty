# -*- coding: utf-8 -*-
import example.createGraph as cG
import graph_tool.all as gt
import pandas as pd

features = ["Cll"]#,"Bb","Caa","Cc","Cll","Ff","Kk","Lit","Naa","Nn","Oo","Ti"]

def run(f):
    #files=["CCu.csv","Cuu1.csv"]
    v=pd.read_csv(f,usecols=["Wavelength","Sum"])
    g = cG.create(v)
    print(g)
    
    #graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png")
    for file in features:
        v1=pd.read_csv("data/"+file+".csv",sep=",",usecols=["Wavelength","Sum"])
#        v1=pd.read_csv(files[1],usecols=["Wavelength","Sum"])
        g1 = cG.create(v1)
        #g1 = cG.create("CCu.csv")
        s=gt.similarity(g,g1)
        print(f,"-", file,"benzerlik oranı  \t%",s*100)


run("Numune/Al.csv")
