import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import*
from decimal import Decimal

startrow=221.41
endrow=600.14
 


#http://dataaspirant.com/2015/04/11/five-most-popular-similarity-measures-implementation-in-python/
class Similarity():

    """ Five similarity measures function """

    def euclidean_distance(self,x,y):

        """ return euclidean distance between two lists """

        return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

    def manhattan_distance(self,x,y):

        """ return manhattan distance between two lists """

        return sum(abs(a-b) for a,b in zip(x,y))

    def minkowski_distance(self,x,y,p_value):

        """ return minkowski distance between two lists """

        return self.nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),
           p_value)

    def nth_root(self,value, n_root):

        """ returns the n_root of an value """

        root_value = 1/float(n_root)
        return round (Decimal(value) ** Decimal(root_value),3)

    def cosine_similarity(self,x,y):

        """ return cosine similarity between two lists """

        numerator = sum(a*b for a,b in zip(x,y))
        denominator = self.square_rooted(x)*self.square_rooted(y)
        return round(numerator/float(denominator),3)

    def square_rooted(self,x):
        return round(sqrt(sum([a*a for a in x])),3)

    def jaccard_similarity(self,x,y):
        intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
        union_cardinality = len(set.union(*[set(x), set(y)]))
        return intersection_cardinality/float(union_cardinality)




data=pd.read_csv("data/prepareData.csv",index_col=0,sep=",")
f=pd.read_csv("Numune/Cu.csv",sep=",",index_col=0,usecols=["Wavelength","Sum"])
#f=f[startrow:endrow,1:]
f=f.T
score = {
"cos":0.0,
"euclidean":1624458000,
"manhattan":1624458000,
"minkowski":1624458000,
"jaccard":0.0
}
sim = {
"cos":"",
"euclidean":"",
"manhattan":"",
"minkowski":"",
"jaccard":""
}

x=data.iloc[0,startrow:endrow]
print(x)
def run(f):    
    value=0.0
    measures = Similarity()
    for column in data: 
        x,y=data[startrow:endrow][column],f[1:][startrow:endrow]
        
        value=measures.cosine_similarity(x,y)
        if value>score["cos"]:
            sim["cos"]=column;
            score["cos"]=value        
        
        value=measures.jaccard_similarity(x,y)
        if value>score["jaccard"]:
            sim["jaccard"]=column;
            score["jaccard"]=value
        
        value=measures.euclidean_distance(x,y)
        if value<score["euclidean"]:
            sim["euclidean"]=column;
            score["euclidean"]=value
            
        value=measures.manhattan_distance(x,y)
        if value<score["manhattan"]:
            sim["manhattan"]=column;
            score["manhattan"]=value
        
        value=measures.minkowski_distance(x,y,3)
        if value<score["minkowski"]:
            sim["minkowski"]=column;
            score["minkowski"]=value
        
 
run(f)
print(sim)
print(score)
