#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 10.11
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "version1" and "version2" should both return a list with all words
# in words.txt
# 
# 1. Two words are a "reverse pair" if each is the reverse of the other. 
# Write a function named "reverse_pair" that returns a list of all the 
# reverse pairs in 'words.txt'. The reverse pairs should be returns in 
# a nested list. 
#

import bisect

def word_list(file):
    fin = open(file)
    li = []

    for line in fin:
        word = line.strip()
        li.append(word)
    return li

# returns true index (distance from left) because bisect is used to determine
# location of insertion
def in_bisect_cheat(word_list, word):
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


def reverse_pair(li):
    list_of_pairs = []
    for word in li:
        if in_bisect_cheat(li, word[::-1]):
            pair = [word, word[::-1]]
            list_of_pairs.append(pair)
    return list_of_pairs


li = word_list("words.txt")