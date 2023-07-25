import pandas as pd

df = pd.read_csv("grades.csv")
"""
print(df.shape)
print(df.head())
print(df.columns)
"""
df2 = df.rename({"Last name":"Last_name", ' "First name"':"First_name", ' "SSN"':"SSN", '"Test1"':"Test1", ' "Test2"':"Test2",
       '"Test3"':"Test3", '"Test4"':"Test4", '"Final"':"Final", '"Grade"':"Grade"})
print(df2.columns)
print(df.iloc[:3])

df3 = df2.drop(range(5),axis = 0)
print(df3)
print(df3.loc[6])
