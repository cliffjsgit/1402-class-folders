#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 9.6
#
#
# Grading Guidelines:
# - No answer variables needed. Grading script will call function.
# - Function 'is_abecedarian' should return boolean True/False depending on if
# the letters are in alphabetical order.
#
# 1. Write a function called is_abecedarian that returns True if the letters in
# a word appear in alphabetical order (double letters are ok).
# 

def is_abecedarian(word):
    previous_letter = word[0]
    for letter in word:
        if ord(letter) < ord(previous_letter):
            return False
        previous_letter = letter
    return True