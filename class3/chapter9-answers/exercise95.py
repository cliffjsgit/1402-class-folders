#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 9.5
#
#
# Grading Guidelines:
# - No answer variable needed for question 1. Grading script will call function.
# Variable 'answer2' is needed for answer 2.
# - Function 'uses_all' should return boolean True/False depending on if
# all the letters specified are in the word. 
# - Variable 'answer2' should be the number of word that use all the vowels 
# "aeiou".
#
# 1. Write a function named uses_all that takes a word and a string of required 
# letters, and that returns True if the word uses all the required letters at 
# least once.
#
# 2. How many words are there that use all the vowels aeiou? How about
# aeiouy?
#
def uses_all(word, letters):
    for letter in letters:
        if letter not in word:
            return False
    return True

fin = open('words.txt')
count = 0

for line in fin:
    word = line.strip()
    if uses_all(word, ['a','e','i','o','u','y']):
        count += 1

answer2 = count