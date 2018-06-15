import pandas as pd
import re

doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)
df.head(10)


def date_sorter():
    # Your code here
    i = 0
    for t in df:
        curr = re.findall(r'(?:\d{1,2} )?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[.,]?[ ]?(?:\d{1,2}[,]? )?[12]\d{3}', t)
        curr2 = re.findall(r"\d{1,2}[/-]\d{1,2}[/-](?:\d{2}(?!\d)|[12]\d{3})|(?:\d{1,2}[/-])?[12]\d{3}", t)
        print(str(i) + " ", end="")
        if len(curr2) >= 2 or len(curr) >= 2:
            print(t.strip())
        elif len(curr) == 0:
            print("f", end="")
            print(curr2)
        else:
            print(curr)

        i += 1

    return  # Your answer here


date_sorter()
