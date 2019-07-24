#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 13.1
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "strip_and_lower" will not be checked aside from ability to run.
#
# 1. Write a function named "strip_and_lower" that reads "emma.txt", breaks each 
# line into words, strips whitespace and punctuation from the words, and 
# converts them to lowercase. Nothing should be returned at this time. 
#
# Hint: The string module provides a string named "whitespace", which contains 
# space, tab, newline, etc., and "punctuation" which contains the punctuation
# characters. Let's see if we can make Python swear:
#
# >>> import string
# >>> string.punctuation
# '!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'
#

import string

def strip_and_lower(file):
    fp = open(file)
    
    for line in fp:
        line = line.replace('-', ' ')
        strippables = string.punctuation + string.whitespace
    
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            
strip_and_lower("emma.txt")