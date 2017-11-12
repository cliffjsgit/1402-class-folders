#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 12.3\n")
#
# Question 1
# 1. Two words form a "metathesis pair" if you can transform one into the other 
# by swapping two letters; for example, "converse" and "conserve". Write a 
# program that finds all of the metathesis pairs in the dictionary. Hint: don't
# test all pairs of words, and don't test all possible swaps. 
#
import anagram_sets


def metathesis_pairs(d):
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1, word2)


def word_distance(word1, word2):
    assert len(word1) == len(word2)

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count


if __name__ == '__main__':
    sets = anagram_sets.all_anagrams('words.txt')
    metathesis_pairs(sets)