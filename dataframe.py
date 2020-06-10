import pandas as pd
import numpy as np
#a=np.array([[1,2,3],[4,5,6]])
#b=pd.DataFrame(a)
#a=np.array([[1,2,3],[4,5,6]])
#b=pd.DataFrame(a,index=['one','two'],columns=['faya','gous','azam'])
#print(b)
#print(b['faya'])
#print(b.columns)
#a=np.random.randn(25).reshape(5,5)
#print(a)
#a=pd.Series(np.random.randn(5),index=['one','two','three','four','five'])
#print(a)
#print(a.to_frame())
#a=pd.Series([1,2,3,4,5])
#print(a)
#b=pd.Series([6,7,8,9,10])
#print(b)
#c=pd.concat([a,b],axis=1)
#print(c)
#print(c.iloc[0])
#print(c.iloc[0][0])
#print(c.columns)
#a=pd.DataFrame([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],index=['zero','one','two','three','four'],columns=['zero','one','two','three','four'])
#print()
"""
#print(a.drop(['two','four']))
#print(a.drop(['two','four'],axis=1))
#print(a.describe())
#print(a.transpose())
#print(a.transpose().describe())
print(a.describe().sum(axis=1))
print(a.sum(axis=0))
print(a.max(axis=1))
print(a.max(axis=0))
print(a.min(axis=1))
print(a.min(axis=0))
"""
#print(a)
#print(a.cumsum(axis=1))
#print(a.cumsum())

student={
    'name':['sachin','rohit','malinga','pandya','pollard','sachin'],
    'popularity':['cricket','chess','ludo','police','police','cricket'],
    'rank':[1,2,3,4,5,1]
}
a=pd.DataFrame(student,index=['zero','first','second','third','fourth','fifth'],columns=['name','popularity','rank'])
print(a.to_csv("Student.csv",index=False))
#print(a[a['name']=='malinga'])
#print(a[a['popularity']!='chess'])
#print(a[(a['name']=='rohit')| (a['rank']==3)])
#print(a)
#print(a.duplicated())
#print(a.duplicated(['popularity','rank']))
#print(a.duplicated())
#print(a.drop_duplicates(keep='last'))
#print(a.drop_duplicates())
#print(a.drop('first',axis=0))
"""
print(a.iloc[3,0])
print(a.loc['third','name'])
print(a.iat[3,0])
print(a.at['third','name'])
print(a[1:3])
"""








