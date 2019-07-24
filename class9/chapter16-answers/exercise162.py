#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 16.2
#
#
# 1. The datetime module provides time objects that are similar to the Time 
# objects in this chapter, but they provide a rich set of methods and operators.
# Read the documentation at http://docs.python.org/3/library/datetime.html.
#

from Time1 import *
from datetime import datetime
#
# 2. Use the datetime module to write a program that gets the current date and 
# prints the day of the week. Write a program that takes a birthday as input and
# prints the user's age and the number of days, hours, minutes and seconds until
# their next birthday.
#
print("Today's date and the day of the week:")
today = datetime.today()
print(today)
print(today.strftime("%A"))

print("Your next birthday and how far away it is:")
#s = input('Enter your birthday in mm/dd/yyyy format: ')
s = '5/11/1967'
bday = datetime.strptime(s, '%m/%d/%Y')

next_bday = bday.replace(year=today.year)
if next_bday < today:
    next_bday = next_bday.replace(year=today.year+1)
print(next_bday)

until_next_bday = next_bday - today
print(until_next_bday)

print("Your current age:")
last_bday = next_bday.replace(year=next_bday.year-1)
age = last_bday.year - bday.year
print(age)
#
# 3. For two people born on different days, there is a day when one is twice as 
# old as the other. That's their Double Day. Write a program that takes two 
# birthdays and computes their Double Day.
#
print("For people born on these dates:")
bday1 = datetime(day=11, month=5, year=1967)
bday2 = datetime(day=11, month=10, year=2000)
print(bday1)
print(bday2)

print("Double Day is")
d1 = min(bday1, bday2)
d2 = max(bday1, bday2)
dd = d2 + (d2 - d1)
print(dd)
#
# 4. For a little more challenge, write the more general version that computes 
# the day when one person is n times older than the other.
# 
n = 3
print("{} Day is".format(n))
d1 = min(bday1, bday2)
d2 = max(bday1, bday2)
dd = d2 + (d2 - d1)*(n-1)
print(dd)



