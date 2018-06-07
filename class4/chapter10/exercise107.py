#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 10.7
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "has_duplicates" should return True if a list has duplicates
# or False if not.
#
# 1. Write a function called has_duplicates that takes a list and returns True
# if there is any element that appears more than once. It should not modify the
# original list.
#
def has_duplicates(li):
    if len(li) == 0:
        return "List is empty."
    elif len(li) == 1:
        return "List contains only one element."
    
    previous_elem = li[0]
    for elem in sorted(li):
        if previous_elem == elem:
            return True
        previous_elem = elem
    return False