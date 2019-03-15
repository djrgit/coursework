#! /usr/bin/env python
# -*- coding; utf-8 -*-

from datetime import date
from datetime import datetime
from datetime import timedelta

# datetime
today = datetime.today()
print()
print("Today: ", today)
print()

# date
todaydate = date.today()
year = todaydate.year
month = todaydate.month
day = todaydate.day
print("Today's Date:  ", todaydate)
print('Current Year:  ', year)
print('Current Month: ', month)
print('Current Day:   ', day)
print()

# timedelta objects
nye = date(year, 12, 31)
days_til_nye = nye - todaydate
add_a_day = timedelta(days=1)

ny = nye + add_a_day
print("New Year's Day: ", ny)
print()

if nye is not todaydate:
    print("There are still " + str(days_til_nye.days) + " days until New Year's Eve...")
else:
    print("It's New Year's Eve - Time to party!")

print()
