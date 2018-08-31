import pandas as pd
import numpy as np# -*- coding: utf-8 -*-

features = ["All","Bb","Caa","Cc","Cll","Ff","Kk","Lit","Naa","Nn","Oo","Ti"]
wavelength=pd.read_csv("data/AllData.csv",index_col=0,sep=";",usecols=["Wavelength"])
data=pd.DataFrame(columns=features,index=wavelength.index)
data.head()

for file in features:
    f=pd.read_csv("data/"+file+".csv",sep=",",index_col=0,usecols=["Wavelength","Sum"])
    for row in f.index:    
        if row in wavelength.index:
            data.loc[row,file]=float(f.loc[row,"Sum"])

data.to_csv("data/full.csv")


