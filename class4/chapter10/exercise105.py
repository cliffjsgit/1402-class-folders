#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 10.5
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "is_sorted" should return True if list is sorted ascending
# or False if otherwise.
#
# 1. Write a function called is_sorted that takes a list as a parameter and 
# returns True if the list is sorted in ascending order and False otherwise. 
# For example:
#
# >>> is_sorted([1, 2, 2])
# True
# >>> is_sorted(['b','a'])
# False
#
def is_sorted(li):
    return li == sorted(li)