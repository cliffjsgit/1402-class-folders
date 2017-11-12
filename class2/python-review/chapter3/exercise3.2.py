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
print("Exercise 3-2\n")
#
# A function object is a value you can assign to a variable or pass as an 
# argument. For example, do_twice is a function that takes a function object as 
# an argument and calls it twice:\n")
#
# def do_twice(f):
#     f()
#     f()
#
# Here's an example that uses do_twice to call a function named print_spam 
# twice:
#
# def print_spam():
#     print('spam')
#     do_twice(print_spam)
#
# Question 1
# 1. Type this example into a script and test it.
#
def do_twice(f):
    f()
    f()
def print_spam():
    print('spam')
    do_twice(print_spam)
#print_spam()
# This function causes an infinite loop
#
# Question 2
# 2. Modify do_twice so that it takes two arguments, a function object and a 
# value, and calls the function twice, passing the value as an argument.
#
# Note: you will need rename the function to "do_twice_2"
#
def do_twice2(f,v):
    f(v)
    f(v)
#
# Question 3
# 3. Copy the definition of print_twice from earlier in this chapter to your 
# script.
#
# def print_twice(bruce):
#     print(bruce)
#     print(bruce)
#
def print_twice(bruce):
    print(bruce)
    print(bruce)
#
# Question 4
# 4. Use the modified version of do_twice to call print_twice twice, passing 
# 'spam' as an argument.
#
do_twice2(print_twice,"spam")
#
# Question 5
# 5. Define a new function called do_four that takes a function object and a 
# value and calls the function four times, passing the value as a parameter. 
# There should be only two statements in the body of this function, not four
#
def do_four(f,v):
    do_twice2(f,v)
    do_twice2(f,v)
do_four(print_twice,"spam")