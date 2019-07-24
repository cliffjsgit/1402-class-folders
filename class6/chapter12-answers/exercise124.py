#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 12.4
#
#
# Grading Guidelines:
# - Variable "answer" should be the longest word fitting the puzzle requirements
#
# 1. Here's another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):
# What is the longest English word, that remains a valid English word, as you 
# remove its letters one at a time?
#
# Now, letters can be removed from either end, or the middle, but you can't 
# rearrange any of the letters. Every time you drop a letter, you wind up with 
# another English word. If you do that, you're eventually going to wind up with 
# one letter and that too is going to be an English word-one that's found in the
# dictionary. I want to know what's the longest word and how many letters does 
# it have?
# 
# I'm going to give you a little modest example: Sprite. Ok? You start off with 
# sprite, you take a letter off, one from the interior of the word, take the r 
# away, and we're left with the word spite, then we take the e off the end, 
# we're left with spit, we take the s off, we're left with pit, it, and I.
# 
# Write a program to find all words that can be reduced in this way, and then 
# find the longest one.
# 
# This exercise is a little more challenging than most, so here are some 
# suggestions:
# 
# 1. You might want to write a function that takes a word and computes a list of
# all the words that can be formed by removing one letter. These are the 
# "children" of the word.
# 
# 2. Recursively, a word is reducible if any of its children are reducible. As a
# base case, you can consider the empty string reducible.
# 
# 3. The wordlist I provided, words.txt, doesn't contain single letter words. So
# you might want to add "I", "a", and the empty string.
# 
# 4. To improve the performance of your program, you might want to memoize the 
# words that are known to be reducible.

answer = None

def make_word_dict():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d

memo = {}
memo[''] = ['']


def is_reducible(word, word_dict):
    if word in memo:
        return memo[word]
    res = []
    for child in children(word, word_dict):
        if is_reducible(child, word_dict):
            res.append(child)
    memo[word] = res
    return res


def children(word, word_dict):
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)
    return res


def all_reducible(word_dict):
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res


def print_trail(word):
    if len(word) == 0:
        return
    print(word, end=' ')
    t = is_reducible(word, word_dict)
    print_trail(t[0])


def print_longest_words(word_dict):
    words = all_reducible(word_dict)
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)
    for _, word in t[0:5]:
        print_trail(word)
        print('\n')

if __name__ == '__main__':
    word_dict = make_word_dict()
    print_longest_words(word_dict)