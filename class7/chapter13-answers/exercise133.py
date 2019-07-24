#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 13.3
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "strip_and_lower" should return a list of the 20 most frequently
# used words in the book in order of usage, decending.
# 
# Question 1
# 1. Modify the function from the previous exercise to return a list of the
# 20 most frequently used words in the book in order of usage, decending. 
#

import string

def strip_and_lower(file):
    hist = {}
    fp = open(file)
    
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break
    for line in fp:
        line = line.replace('-', ' ')
        strippables = string.punctuation + string.whitespace
    
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1
    
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    l = []
    for value, key in t:
        l.append(key)
    return l[:20]

strip_and_lower("emma.txt")