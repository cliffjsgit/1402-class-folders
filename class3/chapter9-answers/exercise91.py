#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 9.1
#
#
# Grading Guidelines:
# - Variable 'answer' must be a list containing 3 words
# - List does not have to be in alphabetical order (but will be sorted)
# - Words must remain unaltered from file (e.g. lower case, no whitespace, etc)
#
# Answer Example: 
# - answer = ['aWord', 'anotherWord', 'oneMoreWord']
#
# 1. Write a program that reads words.txt and adds the words with more 
# than 20 characters (not counting whitespace) to a list which is returned
# by the function.
#

def main():
    answer = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            answer.append(word)
    return answer

if __name__ == '__main__':
    main()
    