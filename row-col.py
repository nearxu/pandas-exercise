import numpy as np
import pandas as pd


data = [[1, 2, 3], [4, 5, 6]]
index = ['a', 'b']
columns = ['A', 'B', 'C']
df = pd.DataFrame(data=data, index=index, columns=columns)

print(df)

df1 = df.set_index('A', drop=True, append=False)
df2 = df.set_index(['A', 'C'], drop=False, append=True)
print(df1)

print(df2)
