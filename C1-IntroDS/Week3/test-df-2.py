import pandas as pd
import numpy as np
df = pd.read_csv('census.csv')

# Idiomatic Solution

print(df.head())

# Method Chaining

print(df.where(df["SUMLEV"] == 50).dropna().set_index(["STNAME", "CTYNAME"]).rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}).head())

# Drop Example

# print(df.drop(df[df['Quantity'] == 0].index).rename(columns={'Weight': 'Weight (oz.)'}))


def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]

    return pd.Series({'min': np.min(data), 'max': np.max(data)})


print(df.apply(min_max, axis=1))

rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']
df.apply(lambda x: np.max(x[rows]), axis=1)



