#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 5-3\n")
# If you are given three sticks, you may or may not be able to arrange them in 
# a triangle. For example, if one of the sticks is 12 inches long and the other
# two are one inch long, you will not be able to get the short sticks to meet 
# in the middle. For any three lengths, there is a simple test to see if it is 
# possible to form a triangle:
#
#     If any of the three lengths is greater than the sum of the other two, then
#     you cannot form a triangle. Otherwise, you can. (If the sum of two lengths
#     equals the third, they form what is called a "degenerate" triangle.)"
#
# Question 1
# 1. Write a function named is_triangle that takes three integers as arguments, 
# and that prints either "Yes" or "No", depending on whether you can or cannot 
# form a triangle from sticks with the given lengths
#
def is_triangle(x,y,z):
    if x > y + z or y > x + z or z > x + y:
        print("No")
    else:
        print("Yes")

#
# Question 2
# 2. Write a function that prompts the user to input three stick lengths, 
# converts them to integers, and uses is_triangle to check whether sticks with 
# the given lengths can form a triangle.
#
def ask_triangle():
    a = input("Type length of side a: ")
    b = input("Type length of side b: ")
    c = input("Type length of side c: ")
    
    is_triangle(int(a), int(b), int(c))
answer1=ask_triangle()
