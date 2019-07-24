#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 10.3
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "middle" should output all list elements, but first and last. 
#
# 1. Write a function called middle that takes a list and returns a new list 
# that contains all but the first and last elements. For example:
#
# >>> t = [1, 2, 3, 4]
# >>> middle(t)
# [2, 3]
#
def middle(li):
    return li[1:-1]