import pandas as pd

url="https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv"

data = pd.read_csv(url)
"""
print(data[["City","Time"]].head())

print(data.isnull().head(10))
print(data.notnull().head(10))

print(data.isnull().sum())   #sayısal veri alma
print(data[data.City.isnull()])

# ---- Dropna
print(data)
data =data.dropna(how ="any")   # all da kullanılabilir
print(data.shape)
"""
data = data.dropna(subset=["City","Colors Reported"],how ="all")
print(data.shape)
print(data)