#code demonstration of Pandas library 
import pandas as pd
a = {'Student':['David', 'Samuel', 'Terry', 'Evan'],
     'Age':['27', '24', '22', '32'],
     'Country':['UK', 'Canada', 'China', 'USA'],
     'Course':['Python','Data Structures','Machine Learning','Web Development'],
     'Marks':['85','72','89','76']}
df=pd.DataFrame(a)
print(df)
c=df[["Country","Course"]]
print(c)
