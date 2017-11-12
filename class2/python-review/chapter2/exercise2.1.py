#!/usr/bin/env python3

###############################################################################
# As with exercise 1, I would suggest that you do these in the file again. If 
# you need, you can do them in the interpreter. Ultimately this python file 
# should look like the following:
#
# print("1. Use python to show the addition of 1+1.")
# answer1 = 1+1
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
print("\nExercise 2-1\n")
#
# Repeating my advice from the previous chapter, whenever you learn a new
# feature, you should try it out in interactive mode and make errors on purpose 
# to see what goes wrong.
#
# Question 1
# 1. We've seen that n = 42 is legal. What about 42 = n?
#
answer1="SyntaxError: can't assign to literal"
print("Answer:\t{}\n".format(answer1))
#
# Question 2
# 2. How about x = y = 1?
# 
x=y=1
answer1=x
answer2=y
print("Value of x:\t{}\nValue of y:\t{}\n".format(answer1, answer2))
#
# Question 3
# 3. In some languages every statement ends with a semicolon, ;. What happens 
# if you put a semicolon at the end of a Python statement? (print some 
# arbitrary value assigned with ';' at the end)
#
answer1=x;
print("Answer:\t{}\n".format(answer1))
#
# Question 4
# 4. What if you put a period at the end of a statement?
#
answer1="SyntaxError: invalid syntax"
print("Answer:\t{}\n\n".format(answer1))