#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 13.2
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "strip_and_lower" should return a histogram in the form of a
# dictionary where the key is the word and the value is the number of times
# it occured.
#
# 1. Modify your function from the previous exercise to skip over the header 
# information at the beginning of the file, and process the rest of the words 
# as before. Then modify the function to count the total number of words in 
# the book, and the number of times each word is used. Use a histogram to
# collect this info and return that dictionary -- where the key is the word 
# and the value is the number of times it occured. 
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
    return hist
    
strip_and_lower("emma.txt")