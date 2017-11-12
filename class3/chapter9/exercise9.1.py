#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 9.1\n")
#
# Question 1
# 1. Write a program that reads words.txt and prints only the words with more 
# than 20 characters (not counting whitespace).
#
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)