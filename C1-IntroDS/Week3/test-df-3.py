import pandas as pd
import numpy as np

df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]

for state in df["STNAME"].unique():
    print(state)

for group, frame in df.groupby("STNAME"):
    avg = np.average(frame['CENSUS2010POP']) # faster
    # avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP']) # slower
    print('Counties in state ' + group + ' have an average population of ' + str(avg))

print(df.groupby('STNAME').agg({'CENSUS2010POP': np.average}))

print(df.groupby("STNAME").agg({["CENSUS2010POP", "CENSUS2010POP"]: np.multiply}))


# print(df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))

# Or alternatively without using a lambda:
# def totalweight(df, w, q):
#        return sum(df[w] * df[q])
#
# print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))

print(type(df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']))
print(type(df.groupby(level=0)['POPESTIMATE2010']))


(df.set_index('STNAME').groupby(level=0)['CENSUS2010POP']
    .agg({'avg': np.average, 'sum': np.sum}))

(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    .agg({'avg': np.average, 'sum': np.sum}))

(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    .agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum}))

