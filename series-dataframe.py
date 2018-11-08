import pandas as pd
import numpy as np

data = [1, 2, 3]
index = ['a', 'b', 'c']
s = pd.Series(data=data, index=index, name='sss')

# dataFrame

data = [[1, 2, 3],
        [4, 5, 6]]
index = ['a', 'b']
columns = ['A', 'B', 'C']
df = pd.DataFrame(data=data, index=index, columns=columns)


tips = pd.read_csv('data/tips.csv')

print(tips.head())
