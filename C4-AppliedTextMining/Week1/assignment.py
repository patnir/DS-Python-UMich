import pandas as pd
import re

doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)
df.head(10)


def get_all_dates():
    all_dates = []
    for t in df:
        curr = re.findall(r'(?:\d{1,2} )?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[.,]?[ ]?(?:\d{1,2}[,]? )?[12]\d{3}',t)
        curr2 = re.findall(r"\d{1,2}[/-]\d{1,2}[/-](?:\d{2}(?!\d)|[12]\d{3})|(?:\d{1,2}[/-])?[12]\d{3}", t)
        if len(curr) == 0:
            all_dates.append(curr2)
        else:
            all_dates.append(curr)

    return all_dates


def get_all_dates_named():
    i = 0
    all_dates = []
    for t in df:

        curr2 = re.match(r"(?P<month>\d{1,2})[/-](?P<day>\d{1,2})[/-](?P<year>\d{2}(?!\d)|[12]\d{3})|(?:(?P<month1>\d{1,2})[/-])?(?P<year1>[12]\d{3})", t)
        if curr2 != None:
            print(str(i) + " " + t.strip())
            print(curr2.groups())
            print()
        i += 1

    return all_dates


def test_func():
    t = "Lithium 0.25 (7/11/77). (7/11/77) LFTS wnl.  Urine tox neg.  Serum tox + fluoxetine 500; otherwise neg.  TSH 3.28.  BUN/Cr: 16/0.83.  Lipids unremarkable.  B12 363, Folate >20.  CBC: 4.9/36/308 Pertinent Medical Review of Systems Constitutional:"
    curr2 = re.compile(r"(?P<month>\d{1,2})[/-](?P<day>\d{1,2})[/-](?P<year>\d{2}(?!\d)|[12]\d{3})")
    for i in curr2.finditer(t):
        print(i.groupdict())


def date_sorter():
    print(get_all_dates())

    return  # Your answer here


test_func()
# print(df[72])
