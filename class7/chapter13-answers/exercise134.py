#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 13.4
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "strip_and_lower" should return a list of words in the book that
# are not in the word list. 
# 
# 1. Modify the previous program to read "words.txt" and then return a list 
# of words in the book that are not in the word list. 
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
    dictionary = {}
    fin = open("words.txt")
    
    for word in fin:
        dictionary[word.strip()] = 0
        
    res = {}
    for key in hist:
        if key not in dictionary:
            res[key] = None
    return res

print(strip_and_lower("emma.txt"))