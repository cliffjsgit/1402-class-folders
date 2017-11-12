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
print("\nExercise 1-2\n")
# 
# Start the Python interpreter and use it as a calculator.
# Question 1
# 1. How many seconds are there in 42 minutes 42 seconds?
#
answer1=(42*60)+42
print("Answer:\t{:01.0f}\n".format(answer1))
#
# Question 2
# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers 
# in a mile.
#
answer1=10/1.61
print("Answer:\t{:03.2f}\n".format(answer1))
#
# Question 3
# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your 
# average pace (time per mile in minutes and seconds)? What is your average
# speed in miles per hour?")
#
answer1=((42*60)+42)/(10/1.61)/60
answer2=60/answer1
print("Min per mile:\t{:03.2f}\nMPH:\t\t{:03.2f}\n".format(answer1,answer2))    