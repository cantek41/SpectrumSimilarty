# -*- coding: utf-8 -*-
import createGraph as cG
import graph_tool.all as gt

#files=["CCu.csv","Cuu1.csv"]
files=["../Numune/Al.csv","../data/All.csv"]

g = cG.create(files[0])
print(g)

#graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,output_size=(200, 200), output="two-nodes.png")

g1 = cG.create(files[1])
#g1 = cG.create("CCu.csv")
s=gt.similarity(g,g1)
print(files[0],"- ile -", files[1],"benzerlik oranı : %",s*100)



