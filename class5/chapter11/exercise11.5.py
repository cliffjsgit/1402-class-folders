#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 11.5\n")
#
# Question 1
# 1. Two words are "rotate pairs" if you can rotate one of them and get 
# the other (see rotate_word in Exercise 8.5).
# 
# Write a program that reads a wordlist and finds all the rotate pairs.
#

def make_dict(fin):
    fin=open('words.txt')
    mydict=dict()
    wlist=[]
    for line in fin:
        word = line.strip()
        wlist.append(word)
    index = 0
    for word in wlist:
        mydict[word] = index
        index += 1
    return mydict

def rotate_word(word, n):
    rotated_word = ''
    for letter in word:
        rotated_word += chr(ord(letter) + n)
    return rotated_word

def rotate_pair(mydict):
    pair = {}
    for n in range(1, 26):  
        for word in mydict:
            if rotate_word(word, n) in mydict:
                if word not in pair:
                    pair[word] = [(rotate_word(word, n), n)]
                else:
                    pair[word].append((rotate_word(word, n), n))
                    
    return pair             


mydict = make_dict("words.txt")
print(rotate_pair(mydict))