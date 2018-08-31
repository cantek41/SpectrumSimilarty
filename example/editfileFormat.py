import pandas as pd
g = pd.read_excel("All2.xlsx")
print(g)
s=g.reset_index()
#print(g)
g.to_csv("AllCu.csv",sep = ',')
