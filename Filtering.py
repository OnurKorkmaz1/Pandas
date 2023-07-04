
import pandas as pd

films = pd.read_csv("imdb_1000.csv")
#print(films)
print(films.columns)
print(films.head())

# Filtering
"""
print(films[films["star_rating"]>8.5][["title","star_rating"]])

print(films[(films["star_rating"]>8.5)&(films["star_rating"]<=9.0)][["title","star_rating"]])
"""
# or kullanımı
#print(films[(films["star_rating"]>8.5)|(films["star_rating"]<=9.0)][["title","star_rating"]])


# ---->  Query kullnımı(filtre) < ----- 

print(films.query("star_rating>=9.0 & star_rating <= 9.3")[["title","star_rating"]])