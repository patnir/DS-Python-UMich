import numpy as np
import datetime as dt
import time as tm

a = np.array([1, 2, 3])
print(a)

print(tm.time())
dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow)

print(dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second)

delta = dt.timedelta(days = 100)
print(delta)

today = dt.date.today()
print(today)

print(today - delta)

print(today > today - delta)

