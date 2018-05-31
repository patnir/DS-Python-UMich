import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()


def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]


# print(answer_zero())


def answer_one():
    return df["Gold"].argmax()


print(answer_one())


# Question 2
# Which country had the biggest difference between their summer and winter gold medal counts?
# *This function should return a single string value.*


def answer_two():
    df["Difference"] = abs(df["Gold"] - df["Gold.1"])
    return df["Difference"].argmax()


print(answer_two())


# Question 3
# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative
# to their total gold medal count?
# Only include countries that have won at least 1 gold in both summer and winter.
# *This function should return a single string value.*


def answer_three():
    df["RelDifference"] = abs(df["Gold"].astype(float) - df["Gold.1"].astype(float)) / (df["Gold"].astype(float) + df["Gold.1"].astype(float) + df["Gold.2"].astype(float))
    return df["RelDifference"].dropna().argmax()

    # return df.where((df["RelDifference"] == max(df["RelDifference"])))


# print(answer_three())


def answer_four():
    df["Points"] = 3 * df["Gold.2"] + 2 * df["Silver.2"] + df["Bronze.2"]
    return df["Points"]


# print(answer_four().head(15))