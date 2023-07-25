import pandas as pd

df = pd.read_csv("imdb_1000.csv")

print(df.iloc[df["star_rating"]])
print(df.iloc[:3])
print(df.columns)


print(df.loc[df["star_rating"],"actors_list"])