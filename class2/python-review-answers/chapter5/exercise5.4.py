#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 5-4\n")
#
# Question 1
# 1. What is the output of the following program? Draw a stack diagram that 
# shows the state of the program when it prints the result.
#
# def recurse(n, s):
#    if n == 0:
#        print(s)
#    else:
#        recurse(n-1, n+s) 
# recurse(3, 0)
#
"""
recurse:
    n -> 3
    s -> 0
recurse:
    n -> 2
    s -> 3
recurse:
    n -> 1
    s -> 5
recurse:
    n -> 0
    s -> 6

Program prints:
6   
"""
#
# Question 2
# 2. What would happen if you called this function like this:
# recurse(-1, 0)?
#
"""
Continues infinitely
"""
# 
# Question 3
# 3. Write a docstring that explains everything someone would need to know in 
# order to use this function (and nothing else).
#
"""
computes value of s
n -> any positive integer
s -> any integer
"""