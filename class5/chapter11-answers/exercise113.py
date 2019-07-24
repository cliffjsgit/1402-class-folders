#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 11.3
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "ackermann" should return an integer
#
# 1. Memoize the "ackermann" function from Exercise 6.2 and see if memoization 
# makes it possible to evaluate the function with bigger arguments. Hint: no.
# 
# def ackermann(m, n):
#     '''Ackermann's function;
#     m, n - integers greater-than-equal 0
#     '''
#     if m == 0:
#         return n + 1
#     elif m > 0 and n == 0:
#         return ack(m - 1, 1)
#     elif m > 0 and n > 0:
#         return ack(m - 1, ack(m, n - 1))
#
# print(ackermann(3, 4))
#

cache = {}

def ackermann(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]



print(ackermann(3, 4))
print(ackermann(3, 6))