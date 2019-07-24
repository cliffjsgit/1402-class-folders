#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 11.1
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "make_dict" should output a dictionary with the words of 
# "words.txt" as keys
#
# 1. Write a function name "make_dict" that reads the words in words.txt,
# stores them as keys in a dictionary and returns the dictionary. It 
# doesn't matter what the values. For simplicity, you can set them to 0. 
#
# This would allow you to use the in operator as a fast way to check whether a 
# word is in the dictionary. If you are feeling ambitious you can compare this
# to the in operator with a list and the bisect search from Chapter 10.
#

def make_dict(file_input):
    dictionary = dict()
    word_list = []
    
    fin = open(file_input)
    for line in fin:
        word = line.strip()
        word_list.append(word)
    
    index = 0
    for word in word_list:
        dictionary[word] = index
        index += 1
    return dictionary


def word_hunter(word, dictionary):
    if word in dictionary:
        return True
    return False


dictionary = make_dict("words.txt")
print(word_hunter('tool', dictionary))
print(word_hunter('cattlee', dictionary))