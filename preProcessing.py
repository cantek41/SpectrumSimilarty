# -*- coding: utf-8 -*-
#veri ön hazırlık
import pandas as pd
startrow=221.41
endrow=600.14

def mainData():   
    file=pd.read_csv("data/full.csv")
    endcolumnValue="600.14"
    endColumIndex=file.columns.get_loc(endcolumnValue)
    file=file.iloc[:,0:endColumIndex]
    file.to_csv("data/prepareData.csv")
    

def guessData():
    pass



