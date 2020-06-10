import pandas as pd
a=pd.read_csv("SacramentocrimeJanuary2006.csv")
#print(a)
#b=(a.groupby(['district']))
b=(dict(list(a.groupby(['district']))))[3]
#print(b)
#print(a.duplicated())
#print(a.drop_duplicates(['district']))
#print(a.describe())
#print(a.info())
#print(a.head())
#print(a.tail())
#print(a['district'])
#print(a.index)