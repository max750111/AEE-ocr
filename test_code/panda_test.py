import pandas as pd

df1 = pd.read_csv('1626250243.csv')
df2 = pd.read_csv('1626250803.csv')

df = df1.append(df2, ignore_index = True)
df.to_csv('output.csv')
print(df)