#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 10.1
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "nested_sum" should output a integer that is a sum of all integers
# in the nested lists.
#
# 1. Write a function called nested_sum that takes a list of lists of integers 
# and adds up the elements from all of the nested lists. For example:
#
# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> nested_sum(t)
# 21
#
def nested_sum(li):
    result = 0
    for elem in li:
        result += sum(elem)
    return result