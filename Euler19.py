## Euler.net problem 19
## You are given the following information, but you may prefer to do some
## research for yourself.
##
## 1 Jan 1900 was a Monday.
## Thirty days has September,
## April, June and November.
## All the rest have thirty-one,
## Saving February alone,
## Which has twenty-eight, rain or shine.
## And on leap years, twenty-nine.
## A leap year occurs on any year evenly divisible by 4, but not on a century
## unless it is divisible by 400.
## How many Sundays fell on the first of the month during the twentieth century
## (1 Jan 1901 to 31 Dec 2000)?

## Must write day of the week function
## Day() will return Mon - Sun
## also write FirstOfTheMonth() which returns True on the first
import datetime

global year, month

countSundays = 0

for year in range(1901,2001,1):
    for month in range(1,13,1):
        if datetime.date(year,month,1).weekday() == 6:
            countSundays +=1
            print('For ',month,', ',year,' the first is a Sunday')

print('Answer = ',countSundays)
