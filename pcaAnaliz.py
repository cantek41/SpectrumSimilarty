# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np# -*- coding: utf-8 -*-
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt


data=pd.read_csv("data/prepareData.csv",index_col=0,sep=",")

#data.fillna(0,inplace=True)
#data.to_csv("data/full.csv")

#element isimlerini sayısala çevirelimki kullanabilelim
elements=data.iloc[:,0:1].values
#cevirim yapalım encoder ile yapacağız
le=preprocessing.LabelEncoder()
elements[:,0]=le.fit_transform(elements[:,0])

#sutuna çevirelim
ohe=preprocessing.OneHotEncoder(categorical_features="all")
elements=ohe.fit_transform(elements).toarray()
#print(elements)

#print(data["Wavelength"].values)


elementSutunları=pd.DataFrame(data=elements,index=range(12),columns=data["Wavelength"].values)

#print(data.iloc[:,1:].values)

x=pd.DataFrame(data=data.iloc[:,1:].values,index=range(12),columns=data.columns.values[1:])

y=data.iloc[:,0:1].values




#artık işleme hazır datayı elde ettik
#veri hazırlık süreci bitti
#islemeHazirData=pd.concat([elementSutunları,dataSutunları],axis=1)
#islemeHazirData.head()

x = preprocessing.StandardScaler().fit_transform(x)

pca = PCA(n_components=2)

principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])

finalDf = pd.concat([principalDf, data[['Wavelength']]], axis = 1)



fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = data["Wavelength"].values

cmap = plt.get_cmap('gnuplot')
colors = [cmap(i) for i in np.linspace(0, 1, 12)]
    
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['Wavelength'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()

#### farklı
xx=pd.DataFrame(data=data.iloc[:,1:].values,index=range(12),
                columns=data.columns.values[1:])
pca1 = PCA(.95)

lower_dimensional_datalower_di  = pca1.fit_transform(xx)

print(pca1.n_components_)


approximationapproxim  = pca.inverse_transform(lower_dimensional_data)



scaled_data=preprocessing.scale(elementSutunları.T)

pca=PCA()

pca.fit(scaled_data)
pca_data=pca.transform(scaled_data)

per_var=np.round(pca.explained_variance_ratio_*100,decimals=1)
labels=["PC"+str(x) for x in range(1, len(per_var)+1)]

plt.bar(x=range(1,len(per_var)+1),height=per_var, tick_label=labels)
plt.ylabel("Percentage of Explained Variance")
plt.xlabel("Principal Companent")
plt.title("Scree Plot")
plt.show()



pca_df=pd.DataFrame(pca_data,columns=labels)
plt.scatter(pca_df.PC1,pca_df.PC2)
plt.xlabel("PC1 -{0}%".format(per_var[0]))
plt.ylabel("PC2 -{0}%".format(per_var[1]))
plt.show()

