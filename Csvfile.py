import pandas as pd

notlar = pd.read_csv("grades.csv")
# veri başlıkları düzgün gelsin istiyorsak
notlar.columns = ["İsim","Soyisim","SSN","Test1","Test2","Test3","Test4","Final","Sonuc"]


print(type(notlar))
print(notlar.head())
print(notlar.tail())
print(notlar["İsim"])
print(notlar.iloc[2])
