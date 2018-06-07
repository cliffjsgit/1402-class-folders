#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 10.6
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "is_anagram" should return True if a word is an anagram
# or False if not.
#
# 1. Two words are anagrams if you can re-arrange the letters from one to spell
# the other. Write a function "is_anagram" that takes two strings and returns
# True if they are anagrams. 
#
def is_anagram(text1, text2):
    return sorted(text1) == sorted(text2)