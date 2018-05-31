import pandas as pd
import numpy as np

df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
print(df)
df.rename(columns={0: 'Grades'}, inplace=True)
print(df)

print(df["Grades"].astype("category").head())

grades = df['Grades'].astype('category',
                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                             ordered=True)

print(grades.head())

print(grades > 'C')

# Ratio Scale: Height and Weight
# Interval Scale: Compass direction
# Ordinal Scale: Letter grades (common in machine learning)
# Nominal Scale: Sport team name

s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])

# Your code here
s = s.astype("category", categories=["Low", "Medium", "High"], ordered=True)
print(s)
print(s>"Low")

df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]

df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
pd.cut(df['avg'],10)
print(df.head(10))

s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])

print(pd.cut(s, 3))


# # You can also add labels for the sizes [Small < Medium < Large].
print(pd.cut(s, 3, labels=['Small', 'Medium', 'Large']))

