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
print("\nExercise 3-3\n")
#
# Note: This exercise should be done using only the statements and other 
# features we have learned so far.
#
# Question 1
# 1. Write a function that draws a grid like the following:
#
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - + 
# |         |         | 
# |         |         | 
# |         |         |
# |         |         | 
# + - - - - + - - - - +
#
def print_four(v):
    print(v)
    print(v)
    print(v)
    print(v)
def draw_grid():
    inter=('+ ' + '- ' * 4) * 2 + '+'
    line='|         |         |'
    print(inter)
    print_four(line)
    print(inter)
    print_four(line)
    print(inter)
draw_grid()
#
# Hint: to print more than one value on a line, you can print a comma-separated 
# sequence of values:
#
#    print('+', '-')
#
# By default, print advances to the next line, but you can override that 
# behavior and put a space at the end, like this:
# 
#        print('+', end=' ')
#        print('-')
#
# The output of these statements is '+ -'.
#
# A print statement with no argument ends the current line and goes to the next
# line.
#
# Question 2
# 2. Write a function that draws a similar grid with four rows and four columns.
#
def draw_double_grid():
    inter=('+ ' + '- ' * 4) * 4 + '+'
    line='|         |         |         |         |'
    print(inter)
    print_four(line)
    print(inter)
    print_four(line)
    print(inter)
    print_four(line)
    print(inter)
    print_four(line)
    print(inter)
draw_double_grid()