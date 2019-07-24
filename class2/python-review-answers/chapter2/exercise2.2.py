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
print("Exercise 2-2\n")
#
# Practice using the Python interpreter as a calculator:
#
# Question 1
# 1.The volume of a sphere with radius r is (4/3)pir^3. What is the volume of a
# sphere with radius 5?
#
from math import pi
answer1=(4.0/3.0)*pi*(5**3)
print("Answer:\t{}\n".format(answer1))
#
# Question 2
# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% 
# discount. Shipping costs $3 for the first copy and 75 cents for each 
# additional copy. What is the total wholesale cost for 60 copies?
#
answer1=24.95*0.6*60+0.75*(60-1)+3
print("Answer:\t{}\n".format(answer1))
#
# Question 3
# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per 
# mile), then 3 miles at tempo (7:12 per mile) and 1 mile at an easy pace again,
# what time do I get home for breakfast?")
#
start = (6*60+52)*60
easy = (8*60+15)*2
fast = (7*60+12)*3
finish_hour = (start + easy + fast)/(60*60.0)
finish_floored = (start + easy + fast)//(60*60)
finish_minute  = (finish_hour - finish_floored)*60
answer1="{}:{}".format(finish_floored,finish_minute)
print("Answer:\t{}\n".format(answer1))
#print("Answer:\t{:%I:%M %p}\n".format(answer1)) # Print for if you decide to use datetime
