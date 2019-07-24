#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 9.4
#
#
# Grading Guidelines:
# - No answer variables needed. Grading script will call function.
# - Function 'uses_only' should return boolean True/False depending on if
# word only uses those letters
#
# 1. Write a function named uses_only that takes a word and a string of letters, 
# and that returns True if the word contains only letters in the list.

def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True