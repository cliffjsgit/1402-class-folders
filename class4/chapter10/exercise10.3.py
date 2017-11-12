#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 10.3\n")
#
# Question 1
# 1. Write a function called middle that takes a list and returns a new list 
# that contains all but the first and last elements. For example:
#
# >>> t = [1, 2, 3, 4]
# >>> middle(t)
# [2, 3]
#
def middle(li):
    return li[1:-1]


t = [1, 2, 3, 4]
ls = middle(t)
print(ls)