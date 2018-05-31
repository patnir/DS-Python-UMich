import pandas as pd

df = pd.read_csv("olympics.csv")
print(df.head())

df = pd.read_csv("olympics.csv", index_col=0, skiprows=1)
print(df.head())

print(df.columns)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col: '#' + col[1:]}, inplace=True)

print(df.head())

print(df["Gold"] > 0)

only_gold = df.where(df["Gold"] > 0)
print(only_gold.head())
print(only_gold['Gold'].count())
print(df['Gold'].count())
only_gold = only_gold.dropna()
print(only_gold.head())

print(len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)]))
print(df[(df['Gold.1'] > 0) & (df['Gold'] == 0)])


