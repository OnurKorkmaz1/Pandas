import pandas as pd
import numpy as np
# Create an Empty Series
s = pd.Series()
print(s)

# Create a Series from ndarray

data = np.array(["a","b","c","d"])

d = pd.Series(data,index= [101,102,103,104])
print(d)

#Create a Series from dict

data2 = {"a":0,"b":1,"c":2}
c = pd.Series(data2)
print(c)