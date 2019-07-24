#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 7.1\n")
#
# Question 1
# 1. Copy the loop from Section 7.5 and encapsulate it in a function called 
# mysqrt that takes a as a parameter, chooses a reasonable value of x, and 
# returns an estimate of the square root of a.
#
# To test it, write a function named test_square_root that prints table like
# this:
#
# a   mysqrt(a)      math.sqrt(a)   diff
# -   ---------      ------------   ----
# 1.0 1.0            1.0            0.0
# 2.0 1.41421356237  1.41421356237  2.22044604925e-16
# 3.0 1.73205080757  1.73205080757  0.0
# 4.0 2.0            2.0            0.0
# 5.0 2.2360679775   2.2360679775   0.0
# 6.0 2.44948974278  2.44948974278  0.0
# 7.0 2.64575131106  2.64575131106  0.0
# 8.0 2.82842712475  2.82842712475  4.4408920985e-16
# 9.0 3.0            3.0            0.0
#
# The first column is a number, a;
# the second column is the square root of a computed with mysqrt;
# the third column is the square root computed by math.sqrt;
# the fourth column is the absolute value of the difference between the two 
# estimates.
#
# pip3 install prettytable
#

def mysqrt(a):
    x = 0.5 * a
    while True:
        estimated_root = 0.5 * (x + a/x)
        if estimated_root == x:
            return estimated_root
        x = estimated_root

def test_square_root(list_of_a):
    import math
    from prettytable import PrettyTable
    t = PrettyTable(['a', 'mysqrt(a)','math.sqrt(a)','diff'])
    
    for a in list_of_a:
        col1 = float(a)
        col2 = mysqrt(a)
        col3 = math.sqrt(a)
        col4 = abs(mysqrt(a) - math.sqrt(a))
        t.add_row([col1,col2,col3,col4])
    print(t)

test_square_root(range(1,10))