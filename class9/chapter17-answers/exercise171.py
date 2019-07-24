#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 17.1
#
#
# 1. Download the code from this chapter from :
#    http://thinkpython2.com/code/Time2.py. 
# Change the attributes of Time to be a single integer representing seconds 
# since midnight. Then modify the methods (and the function int_to_time) to work
# with the new implementation. You should not have to modify the test code in 
# main. When you are done, the output should be the same as before.
#
class Time:
    """Represent instance of time"""

    def __init__(self, hours=0, minutes=0, seconds=0):
        minute = hours * 60 + minutes
        self.seconds = minute * 60 + seconds
    def __str__(self):
        minute, seconds = divmod(self.seconds, 60)
        hours, minutes = divmod(minute, 60)
        return "{:02d}:{:02d}:{:02d}".format(hours,minutes,seconds)
    def __add__(self,other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    def __radd__(self, other):
        return self.__add__(other) 
    def add_time(self,other):
        seconds = self.seconds + other.seconds
        return self.int_to_time(seconds)
    def increment(self,seconds):
        seconds += self.seconds
        return self.int_to_time(seconds)
    def print_time(self):
        print(str(self))
    def time_to_int(self):
        return self.seconds
    def int_to_time(self, seconds):
        return Time(0, 0, seconds)
    def is_after(self,other):
        return self.seconds > other.seconds
        
time = Time(9,12,40)
time2 = Time(1,30,19)
total = sum([time,time2])
print(total)