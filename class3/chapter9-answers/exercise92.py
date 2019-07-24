#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 9.2
#
#
# Grading Guidelines:
# - Variable 'answer' must be a list containing both answers
# - Variable 'answer1' must be a list containing all words without e
# - Variable 'answer2' must be a int or float containing % of words without e
# - Answers will be converted to numbers and graded with a buffer:
# -- 'answer1' +/- 1%
# -- 'answer2' +/- 5%
# 
# Answer Example: 
# - answer1 = ['aWord', 'anotherWord', 'oneMoreWord']
# - answer2 = 28
# - answer = [answer1, answer2]
#
#
# In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby 
# that does not contain the letter "e". Since "e" is the most common letter in `
# English, that's not easy to do.
#
# In fact, it is difficult to construct a solitary thought without using that 
# most common symbol. It is slow going at first, but with caution and hours of 
# training you can gradually gain facility.
# 
# All right, I'll stop now.
# 
# 1. Write a function "has_no_e" that returns True if the given word doesn't 
# have the letter "e" in it. Use the function to create a list of only the
# words that have no "e". Then compute the percentage of words that have no "e".
# Return these as objects in a list "answer".
#

def has_no_e(word):
    e = word.count('e')
    if e > 0:
        return False
    else:
        return True

def main():
    answer1 = [] # list of words w/o e
    answer2 = 0  # percentage of words w/o e

    fin = open('words.txt')
    e_count = 0.0
    n_words = 0.0
    
    for line in fin:
        n_words += 1
        word = line.strip()
        if has_no_e(word) == True:
            e_count += 1
            answer1.append(word)
    answer2 = (e_count/n_words)*100
    answer = [answer1, answer2]
    return answer

if __name__ == '__main__':
    print(main()[1])