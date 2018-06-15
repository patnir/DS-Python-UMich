import pandas as pd
import numpy as np
import re

doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)
df.head(10)


def get_all_dates():
    all_dates_first = []
    all_dates_second = []
    for t in df:
        curr = re.findall(r'(?:\d{1,2} )?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[.,]?[ ]?(?:\d{1,2}[,]? )?[12]\d{3}',t)
        curr2 = re.findall(r"\d{1,2}[/-]\d{1,2}[/-](?:\d{2}(?!\d)|[12]\d{3})|(?:\d{1,2}[/-])?[12]\d{3}", t)
        if len(curr) == 0:
            all_dates_second.append(curr2)
        else:
            all_dates_first.append(curr)

    print(len(all_dates_first))
    print(len(all_dates_second))
    print(len(df))

    return


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
    # t = "Lithium 0.25 (7/11/77). (7/11/77) LFTS wnl.  Urine tox neg.  Serum tox + fluoxetine 500; otherwise neg.  TSH 3.28.  BUN/Cr: 16/0.83.  Lipids unremarkable.  B12 363, Folate >20.  CBC: 4.9/36/308 Pertinent Medical Review of Systems Constitutional:"
    # curr2 = re.compile(r"(?P<month>\d{1,2})[/-](?P<day>\d{1,2})[/-](?P<year>\d{2}(?!\d)|[12]\d{3})")
    # for i in curr2.finditer(t):
    #     print(i.groupdict())

    curr0 = re.compile(r'((?P<day>\d{1,2}) )?(?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[.,]?[ ]?((?P<day1>\d{1,2})[,]? )?(?P<year>[12]\d{3})')
    curr1 = re.compile(r"(?P<month>\d{1,2})[/-](?P<day>\d{1,2})[/-](?P<year>\d{2}(?!\d)|[12]\d{3})")
    curr2 = re.compile(r"(?:(?P<month>\d{1,2})[/-])?(?P<year>[12]\d{3})")

    ans = []

    y = 0

    for t in df[0:500]:
        count0 = len(curr0.findall(t))
        count1 = len(curr1.findall(t))
        count2 = len(curr2.findall(t))

        if count0 != 0:
            for i in curr0.finditer(t):
                # print("curr0 ", end="")
                # print(i.groupdict())
                d = i.groupdict()
                curr = convert_date(y, year=d["year"], month=None, monthname=d["month"], day=d["day"], day1=d["day1"])
        elif count1 != 0:
            for i in curr1.finditer(t):
                # print("curr1 ", end="")
                # print(i.groupdict())
                d = i.groupdict()
                curr = convert_date(y, year=d["year"], month=d["month"], monthname=None, day=d["day"], day1=None)
        else:
            for i in curr2.finditer(t):
                # print("curr2 ", end="")
                # print(i.groupdict())
                d = i.groupdict()
                curr = convert_date(y, year=d["year"], month=d["month"], monthname=None, day=None, day1=None)
        y += 1
        ans.append(curr)
    ans = np.array(ans)
    ans = ans[ans[:, 3].argsort()]
    ans = ans[ans[:, 2].argsort()]
    ans = ans[ans[:, 1].argsort()]
    print(ans[:, 0])


def get_month_number(monthname):
    name = monthname[0:3].lower()
    count = 0
    if name == "jan":
        return 1
    if name == "feb":
        return 2
    if name == "mar":
        return 3
    if name == "apr":
        return 4
    if name == "may":
        return 5
    if name == "jun":
        return 6
    if name == "jul":
        return 7
    if name == "aug":
        return 8
    if name == "sep":
        return 9
    if name == "oct":
        return 10
    if name == "nov":
        return 11
    if name == "dec":
        return 12
    return 0


def convert_date(index, year, month=None, monthname=None, day=None, day1=None):
    y = int(year)
    if y < 100:
        y += 1900
    m = 1

    if month is None and monthname is None:
        m = 1
    elif month is None:
        m = get_month_number(monthname)
    elif monthname is None:
        m = int(month)

    d = 0
    if day is None and day1 is None:
        d = 1
    elif day is None:
        d = int(day1)
    elif day1 is None:
        d = int(day)

    return [index, y, m, d]

def date_sorter():
    print(get_all_dates())

    return  # Your answer here


test_func()
# print(df[72])
