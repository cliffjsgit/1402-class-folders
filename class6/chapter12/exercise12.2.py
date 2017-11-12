#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 12.2\n")
#
# Question 1
# 1. Write a program that reads a word list from a file (see Section 9.1) and 
# prints all the sets of words that are anagrams.
# 
# Here is an example of what the output might look like:
#
# ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
# ['retainers', 'ternaries']
# ['generating', 'greatening']
# ['resmelts', 'smelters', 'termless']
#
# Hint: you might want to build a dictionary that maps from a collection of 
# letters to a list of words that can be spelled with those letters. The 
# question is, how can you represent the collection of letters in a way that 
# can be used as a key?
#

#
# Question 2
# 2. Modify the previous program so that it prints the longest list of anagrams 
# first, followed by the second longest, and so on.
# 

#
# Question 3
# 3. In Scrabble a "bingo" is when you play all seven tiles in your rack, along 
# with a letter on the board, to form an eight-letter word. What collection of 8
# letters forms the most possible bingos? Hint: there are seven.
# 
def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        # TODO: rewrite using defaultdict
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagram_sets_in_order(d):
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))
    t.sort()

    for x in t:
        print(x)


def filter_length(d, n):
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res


if __name__ == '__main__':
    anagram_map = all_anagrams('words.txt')
    print_anagram_sets_in_order(anagram_map)

    eight_letters = filter_length(anagram_map, 8)
    print_anagram_sets_in_order(eight_letters)
    