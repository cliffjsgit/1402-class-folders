#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 9.5\n")
#
# Question 1
# 1. Write a function named uses_all that takes a word and a string of required 
# letters, and that returns True if the word uses all the required letters at 
# least once. How many words are there that use all the vowels aeiou? How about
# aeiouy?
#
def uses_all(word, letters):
    required = letters.split()
    for letter in required:
        if letter not in word:
            return False
    return True


fin = open('words.txt')
count = 0

for line in fin:
    word = line.strip()
    if uses_all(word, 'a e i o u y') == True:
        print(word)
        count += 1
print(count)