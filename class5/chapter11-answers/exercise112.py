#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 11.2
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "invert_dict" should output an inverted dictionary based on a 
# dictionary input.
#
# 1. Read the documentation of the dictionary method setdefault and use it to 
# write a more concise version of invert_dict.
#
# def invert_dict(d):
#     inverse = dict()
#     for key in d:
#         val = d[key]
#         if val not in inverse:
#             inverse[val] = [key]
#         else:
#             inverse[val].append(key)
#     return inverse
#
def invert_dict(d):
    inverse = dict()
    for key in d:
        value = d[key]
        inverse.setdefault(value, []).append(key)
    return inverse