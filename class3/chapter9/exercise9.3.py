#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 9.3\n")
#
# Question 1
# 1. Write a function named avoids that takes a word and a string of forbidden 
# letters, and that returns True if the word doesn't use any of the forbidden 
# letters. Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them. Can
# you find a combination of 5 forbidden letters that excludes the smallest 
# number of words?
#

def avoid(word, forbidden):
    for letter in forbidden:
        if word.count(letter) > 0:
            return False
        else:
            return True


fin = open('words.txt')
count = 0

forbidden_letters = input("Type forbidden letters: ")
forbidden_letters = forbidden_letters.split(" ")
for line in fin:
    word = line.strip()
    if avoid(word, forbidden_letters) == True:
        count += 1

print(count)

# Can you find a combination of 5 forbidden letters
# that excludes the smallest number of words?
# q v y z x 