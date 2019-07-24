#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 5-2\n")
#
# Fermat's Last Theorem says that there are no positive integers a, b, and c
# such that 
#
# a^n + b^n = c^n
# 
# for any values of n greater than 2.
#
# Question 1
# 1. Write a function named check_fermat that takes four parameters a, b, c and 
# n and checks to see if Fermat's theorem holds. If n is greater than 2 and a^n
# + b^n = c^n the program should print, "Holy smokes, Fermat was wrong!" 
# Otherwise the program should print, "No, that doesn't work."
#
def check_fermat(a,b,c,n):
      if n > 2 and (a**n + b**n == c**n):
            print("Holy Smokes, Fermat was wrong!")
      else:
            print("No, that doesn't work.")
#
# Question 2
# 2. Write a function that prompts the user to input values for a, b, c and n,
# converts them to integers, and uses check_fermat to check whether they violate
# Fermat's theorem.
#
def ask_fermat():
      a = input("a: ")
      b = input("b: ")
      c = input("c: ")
      n = input("n: ")
    
      check_fermat(int(a), int(b), int(c), int(n))
ask_fermat()


'''
def ask_fermat():
      a,b,c,n = None,None,None,None
      while a is None:
            try:
                  a = input("a: ")
            except:
                  pass
      while b is None:
            try:
                  b = input("b: ")
            except:
                  pass
      while c is None:
            try:
                  c = input("c: ")
            except:
                  pass
      while n is None:
            try:
                  n = input("n: ")
            except:
                  pass
      check_fermat(int(a), int(b), int(c), int(n))
ask_fermat()
'''