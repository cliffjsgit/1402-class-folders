#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 10.2
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "cum_sum" should output a list of integers that is a stepping 
# cumlative sum of all integers in the nested lists.
#
# 1. Write a function called cum_sum that takes a list of numbers and returns the
# cumulative sum; that is, a new list where the ith element is the sum of the 
# first i + 1 elements from the original list. For example:
# 
# >>> t = [1, 2, 3]
# >>> cumsum(t)
# [1, 3, 6]
#
def cum_sum(li):
    result = []
    total = 0
    for elem in li:
        total += elem
        result.append(total)
    return result