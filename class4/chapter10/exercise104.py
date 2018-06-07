#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 10.4\n")
#
# Question 1
# 1. Write a function called chop that takes a list, modifies it by removing the
# first and last elements, and returns None. For example:
#
# >>> t = [1, 2, 3, 4]
# >>> chop(t)
# >>> t
# [2, 3]
#
def chop(li):
    del li[0]
    del li[-1]