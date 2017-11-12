#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 13.8\n")
#
# Question 1
# 1. "Write a program to read a text from a file and perform Markov analysis. 
# The result should be a dictionary that maps from prefixes to a collection of
# possible suffixes. The collection might be a list, tuple, or dictionary; it 
# is up to you to make an appropriate choice. You can test your program with 
# prefix length 2, but you should write the program in a way that makes it easy
# to try other lengths.
#

#
# Question 2
# 2. Add a function to the "previous program to generate random text based on 
# the Markov analysis. Here is an example from Emma with prefix length 2:
# 
#     He was very clever, be it sweetness or be angry, ashamed or only amused,
#     at such a stroke. She had never thought of Hannah till you were never \
#     meant for me?" "I cannot make speeches, Emma:" he soon cut it all himself.
#
# For this example, I left the punctuation attached to the words. The result is
# almost syntactically correct, but not quite. Semantically, it almost "makes
# sense, but not quite.
# 
# What happens if you increase the prefix length? Does the random text make
# more sense?
# 

#
# Question 3
# 3. Once your program is working, you might want to try a mash-up: if you
# combine text from two or more books, the random text you generate will blend 
# the vocabulary and phrases from the sources in interesting ways.
# 
import sys
import string
import random

# global variables
suffix_map = {}        # map from prefixes to a list of suffixes
prefix = ()            # current tuple of words


def process_file(filename, order=2):
    """Reads a file and performs Markov analysis.

    filename: string
    order: integer number of words in the prefix

    returns: map from prefix to list of possible suffixes.
    """
    fp = open(filename)
    skip_gutenberg_header(fp)

    for line in fp:
        for word in line.rstrip().split():
            process_word(word, order)


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_word(word, order=2):
    """Processes each word.

    word: string
    order: integer

    During the first few iterations, all we do is store up the words; 
    after that we start adding entries to the dictionary.
    """
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
        # if there is no entry for this prefix, make one
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)


def random_text(n=100):
    """Generates random wordsfrom the analyzed text.

    Starts with a random prefix from the dictionary.

    n: number of words to generate
    """
    # choose a random prefix (not weighted by frequency)
    start = random.choice(list(suffix_map.keys()))
    
    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text(n-i)
            return

        # choose a random suffix
        word = random.choice(suffixes)
        print(word, end=' ')
        start = shift(start, word)


def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)


def main(script, filename='emma.txt', n=100, order=2):
    try:
        n = int(n)
        order = int(order)
    except ValueError:
        print('Usage: %d filename [# of words] [prefix length]' % script)
    else: 
        process_file(filename, order)
        random_text(n)
        print()


if __name__ == '__main__':
    main(*sys.argv)