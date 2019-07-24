#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 10.10
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "in_bisect" should return the index in list where the word was
# found
# 
# 1. To check whether a word is in the word list, you could use the in operator,
# but it would be slow because it searches through the words in order. Because 
# the words are in alphabetical order, we can speed things up with a bisection 
# search (also known as binary search), which is similar to what you do when you
# look a word up in the dictionary. You start in the middle and check to see 
# whether the word you are looking for comes before the word in the middle of 
# the list. If so, you search the first half of the list the same way. Otherwise
# you search the second half.
# 
# Either way, you cut the remaining search space in half. If the word list has
# 113,809 words, it will take about 17 steps to find the word or conclude that
# it's not there.
#
# Write a function called in_bisect that takes a sorted list and a target value
# and returns the index of the value in the list if it's there, or None if it's 
# not.
#
import bisect


def make_word_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return i

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i+1:], word)


word_list = make_word_list()