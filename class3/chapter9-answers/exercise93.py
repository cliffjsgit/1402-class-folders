#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 9.3
#
#
# Grading Guidelines:
# - No answer variables needed. Grading script will call functions.
# - Function 'avoids' should return boolean True/False depending on if
# forbidden letters are found
# - Function 'lowest_avoidance' should return a list of 5 lowercase letters
#
#
# 1. Write a function named 'avoids' that takes a word and a string of forbidden 
# letters, and that returns True if the word doesn't use any of the forbidden 
# letters.
# 
# 2. Write a function named 'lowest_avoidance' that finds the 5 letters excluding
#  the fewest number of words and returns them in a list.
#


def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

def get_item(x):
    return x[1]

def lowest_avoidance():
    alpha_list = []
    a = ord('a')
    z = ord('z')
    count = 0
    while a <= z:
        alpha_list.append([chr(a),0])
        a+=1
    for letter in alpha_list:
        for word in open("words.txt"):
            if not avoids(word.strip(),letter):
               alpha_list[count][1] += 1
        count+=1
    top5 = sorted(alpha_list, key=get_item)[:5]
    top5l = []
    for letter in top5:
        top5l.append(letter[0])
    return top5l