#!/usr/bin/env python3

__author__ = "Philip Ulrich"

###############################################################################
#
# Exercise 10.4
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "chop" should remove first and last element in-place. 
#
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