#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 10.9
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "version1" and "version2" should both return a list with all words
# in words.txt
# 
# 1. Write a function named "version1" that reads the file words.txt 
# and builds a list with one element per word. Write a second version
# of this function named "version2" using the idiom t = t + [x]. Which 
# one takes longer to run? Why?
#
def version1(file):
    fin = open(file)
    li = []

    for line in fin:
        word = line.strip()
        li.append(word)
    
    return li


def version2(file):
    fin = open(file)
    t = []
    
    for line in fin:
        x = line.strip()
        t = t + [x]

    return t