import pandas as pd

df = pd.read_csv('dwarf_stars.csv')
df = df.dropna()
print(df.dtypes)
print(df.head())

df['Radius'] = 0.102763*df['Radius']
df["Mass"] = df["Mass"].apply(lambda x:x.replace('$', '').replace(',','')).astype('float')
df['Mass'] = 0.000954588*df['Mass']
print(df.head())

df.drop(['Unnamed: 0'], axis=1, inplace= True)
print(df.head())

df.reset_index(drop=True, inplace=True)
print(df.head())
print(df.dtypes)

df.to_csv('unit_converted_dwarf_stars.csv')