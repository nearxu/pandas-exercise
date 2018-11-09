import pandas as pd

df1 = pd.DataFrame([[1, 2], [3, 4]], index=['a', 'b'], columns=['A', 'B'])
df2 = pd.DataFrame([[1, 3], [4, 8]], index=['b', 'd'], columns=['B', 'C'])


a = pd.merge(left=df1, right=df2, how='inner',
             left_index=True, right_index=True)

# b = pd.concat([df1,df2], join="inner", axis=1)

print(df1)
print(df2)

print(a)
# print(b)
