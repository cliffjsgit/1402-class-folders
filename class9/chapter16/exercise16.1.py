#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 16.1\n")
#
# Question 1
# 1. Write a function called mul_time that takes a Time object and a number and
# returns a new Time object that contains the product of the original Time and 
# the number.
# 
# Then use mul_time to write a function that takes a Time object that represents
# the finishing time in a race, and a number that represents the distance, and 
# returns a Time object that represents the average pace (time per mile).
#

from Time1 import *

def mul_time(t1, factor):
    """Multiplies a Time object by a factor."""
    assert valid_time(t1)
    seconds = time_to_int(t1) * factor
    return int_to_time(seconds)

race_time = Time()
race_time.hour = 1
race_time.minute = 34
race_time.second = 5

print('Half marathon time')
print_time(race_time)

distance = 13.1
pace = mul_time(race_time, 1/distance)

print('Time per mile')
print_time(pace)