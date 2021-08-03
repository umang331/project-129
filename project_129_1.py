import pandas as pd

df = pd.read_csv("dwarf_stars.csv")

print(df.head())

print(df.columns)

df =df = df[df['Star_name'].notna()]
df =df = df[df['Distance'].notna()]
df =df = df[df['Mass'].notna()]
df =df = df[df['Radius'].notna()]

print(df.dtypes)

df["Radius"] = 0.102763*df["Radius"]

df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

df["Mass"] = 0.000954588*df["Mass"]

df.head()

df.columns

df.drop(['Unnamed: 0'],axis=1,inplace=True)

df.head()

df.reset_index(drop=True,inplace=True)

df.to_csv("dwarf_star_2.csv")

df.dtypes