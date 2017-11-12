#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 10.9\n")
#
# Question 1
# 1. Write a function that reads the file words.txt and builds a list with one 
# element per word. Write two versions of this function, one using the append 
# method and the other using the idiom t = t + [x]. Which one takes longer to 
# run? Why?
#
def version1(file):
    fin = open(file)
    li = []

    for line in fin:
        word = line.strip()
        li.append(word)
    
    return li


def version2(file):
    fin = open(file)
    t = []
    
    for line in fin:
        x = line.strip()
        t = t + [x]


#version1("words.txt")
#version2("words.txt")