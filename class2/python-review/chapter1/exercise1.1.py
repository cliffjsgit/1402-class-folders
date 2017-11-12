#!/usr/bin/env python3

###############################################################################
# Below you will find excerpts from our book with the exercises for chapter 1.
# The book suggests that you should do these exercises in the python 
# interpreter. I would suggest that you actually do these in the file. If you
# need, you can do them in the interpreter. Ultimately this python file should
# look like the following:
#
# print("1. Use python to show the addition of 1+1.")
# answer = 1+1
# print("A: {}".format(answer))
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
print("\nExercise 1-1\n")
#
# It is a good idea to read this book in front of a computer so you can try out
# the examples as you go.
#
# Whenever you are experimenting with a new feature, you should try to make mis‐
# takes. For example, in the "Hello, world!" program, what happens if you leave 
# out one of the quotation marks? What if you leave out both? What if you spell
# print wrong?
#
# This kind of experiment helps you remember what you read; it also helps when
# you are programming, because you get to know what the error messages mean. It 
# is better to make mistakes now and on purpose than later and accidentally.
#
# Question 1
# 1. In a print statement, what happens if you leave out one of the parentheses,
# or both?")
#
answer1="SyntaxError: invalid syntax"
answer2="SyntaxError: Missing parentheses in call to 'print'"
print("One parenthesis:\t{}\nNo parentheses:\t\t{}\n".format(answer1, answer2))
#
# Question 2
# 2. If you are trying to print a string, what happens if you leave out one of
# the quotation marks, or both?
#
answer1="SyntaxError: EOL while scanning string literal"
answer2="NameError: name 'hello' is not defined"
print("One quotation:\t{}\nNo quotations:\t{}\n".format(answer1, answer2))
#
# Question 3
# 3. You can use a minus sign to make a negative number like -2. What happens 
# if you put a plus sign before a number? What about 2++2?
#
answer1=-2
answer2=2++2
print("-2:\t{}\n2++2:\t{}\n".format(answer1, answer2))
#
# Question 4
# 4. In math notation, leading zeros are okay, as in 02. What happens if you 
# try this in Python?
#
answer1=02
print("Leading zero:\t{}\n".format(answer1))
#
# Question 5
# 5. What happens if you have two values with no operator between them?")
answer1="NameError: name 'ab' is not defined"
answer2="invalid syntax"
print("No space:\t{}\nSpace:\t\t{}\n\n".format(answer1,answer2))