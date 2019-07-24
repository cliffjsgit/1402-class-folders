#!/usr/bin/env python3

###############################################################################
# As with previous exercises, the solutions should be provided in this file.
# Ultimately this python file should look like the following:
#
# print("1. Use python to show the addition of 1+1.")
# def add(a,b):
#      return a+b
# answer1 = add(1,1)
# print("A: {}".format(answer1))
#
# and the output should be so:
# 
# 1. Use python to show the addition of 1+1.
# A: 2
#
# NOTE: For questions that force you to invoke an error, please invoke the error
# in the interpreter and print the error. For questions that ask you to test if
# something errors and it does not cause an error; print answer as normal.
#
###############################################################################
#
print("\nExercise 3-1\n")
#
# Question 1
# 1. Write a function named right_justify that takes a string named s as a 
# parameter and prints the string with enough leading spaces so that the last 
# letter of the string is in column 70 of the display:")
#
# NOTE: cover https://pyformat.info/
#
def right_justify(rstr):
    return ' ' * (70 - len(rstr)) + rstr
    #return "{0:>70}".format(rstr)
answer1=right_justify("monty")
print("Answer:\n{}\n".format(answer1))
#
# Hint: Use string concatenation and repetition. Also, Python provides a 
# built-in function called len that returns the length of a string, so the 
# value of len('monty') is 5.
#