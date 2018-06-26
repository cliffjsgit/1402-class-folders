#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 13.5
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "choose_from_hist" should return a random value from the 
# histogram, chosen with probability in proportion to frequency
# 
# 1. Write a function named "choose_from_hist" that takes a histogram and 
# returns a random value from the histogram, chosen with probability in 
# proportion to frequency. For example, for this histogram:
#
# >>> t = ['a', 'a', 'b']
# >>> hist = histogram(t)
# >>> hist
# {'a': 2, 'b': 1}
# 
# Your function should return 'a' with probability 2/3 and 'b' with probability 
# 1/3.
#

import string
import random

def choose_from_hist(file):
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
    for word, freq in hist.items():
        t.extend([word] * freq)

    return random.choice(t)
    
print(choose_from_hist("emma.txt"))