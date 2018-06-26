#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 14.2
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "store_anagrams" should take in a dictionary file specified in 
# the arguments, pass it to the function in "anagram_sets" that will generate
# an anagram dictiontionary, and then write it to a shelve.
# - Function "read_anagrams" should take in a shelve file as well as a word
# and then returns a list of anagrams.
# 
# 1. If you download the solution to Exercise 12-2 from 
# http://thinkpython2.com/code/anagram_sets.py, you'll see that it creates a 
# dictionary that maps from a sorted string of letters to the list of words that
# can be spelled with those letters. For example, 'opst' maps to the list 
# ['opts', 'post', 'pots', 'spot', 'stop', 'tops'].
#
# Write a module that imports anagram_sets and provides two new functions: 
# store_anagrams should store the anagram dictionary in a "shelf"; read_anagrams
# should look up a word and return a list of its anagrams.
# 
import shelve
import sys

from anagram_sets import all_anagrams, signature


def store_anagrams(filename, anagram_map):
    """Stores the anagrams from a dictionary in a shelf.

    filename: string file name of shelf
    anagram_map: dictionary that maps strings to list of anagrams
    """
    shelf = shelve.open(filename, 'c')

    for word, word_list in anagram_map.items():
        shelf[word] = word_list

    shelf.close()


def read_anagrams(filename, word):
    """Looks up a word in a shelf and returns a list of its anagrams.

    filename: string file name of shelf
    word: word to look up
    """
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []


def main(script, command='make_db'):
    if command == 'make_db':
        anagram_map = all_anagrams('words.txt')
        store_anagrams('anagrams.db', anagram_map)
    else:
        print(read_anagrams('anagrams.db', command))


if __name__ == '__main__':
    main(*sys.argv)
    