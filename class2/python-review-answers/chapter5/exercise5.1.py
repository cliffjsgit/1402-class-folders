#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 5-1\n")
#
# The time module provides a function, also named time, that returns the current
# Greenwich Mean Time in "the epoch", which is an arbitrary time used as a 
# reference point. On UNIX systems, the epoch is 1 January 1970.
#
# >>> import time
# >>> time.time()
#     1437746094.5735958
#
# Question 1
# 1. Write a script that reads the current time and converts it to a time of day
# in hours, minutes, and seconds, plus the number of days since the epoch.
#
import time
epoch = time.time()

days_since_epoch = int(epoch // (24 * 60 * 60))     # epoch // seconds_in_a_day
hours = int(epoch % (24 * 60 * 60) // 3600)         # (epoch % seconds_in_a_day) // seconds_in_an_hour
minutes = int(epoch % (24 * 60 * 60) % 3600 // 60)  # (epoch % seconds_in_a_day) % seconds_in_an_hour // seconds_in_a_minute
seconds = int(epoch % (24 * 60 * 60) % 3600 % 60)   # (epoch % seconds_in_a_day) % seconds_in_an_hour % seconds_in_a_minute
answer1="{:02d}:{:02d}:{:02d}".format(hours,minutes,seconds)
answer2=days_since_epoch
print("Time (GMT): {}\n".format(answer1)+
      "Days Since epoch: {}".format(answer2))