import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

# Calling DataFrame constructor
df = pd.DataFrame(mydataset)
print(df)


# Python code demonstrate creating 
# DataFrame from dict narray / lists 
# By default addresses.
 
 
# intialise data of lists.
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
 
# Create DataFrame
df1 = pd.DataFrame(data)
 
# Print the output.
print(df1)

# select two columns
print(df1[['Name']])

print(df1.loc[0])

# --------------------------
df2 = pd.DataFrame(data, index = ["day1", "day2", "day3","day4"])
print(df2.loc["day1"])

#Load a comma separated file (CSV file) into a DataFrame:

df3 = pd.read_csv('data.csv')
print(df3) 

#Load the JSON file into a DataFrame:
df4 = pd.read_json('data.json')
print(df4.to_string()) 
