import pandas as pd

df = pd.read_csv("olympics.csv", index_col=0, skiprows=1)

for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
    if col[:1] == '№':
        df.rename(columns={col: '#' + col[1:]}, inplace=True)

# df["country"] = df.index
# print(df.head())
# df = df.set_index("Gold")
# print(df.head())
#
# df = df.reset_index()
# print(df.head())

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

# Your answer here

# Reindex the purchase records DataFrame to be indexed
# hierarchically, first by store, then by person.
# Name these indexes 'Location' and 'Name'.
# Then add a new entry to it with the value of:
# Name: 'Kevyn', Item Purchased: 'Kitty Food', Cost: 3.00 Location: 'Store 2'.

df = df.set_index([df.index, 'Name'])

df.index.names = ['Location', 'Name']

df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))

print(df.head())

