#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 10.8
#
#
# Grading Guidelines:
# - Variable "answer" should be the answer to question 1: If there are 23 
# students in your class, what are the chances that two of you have the 
# same birthday?.
#
# This exercise pertains to the so-called Birthday Paradox, which you can read 
# about at http://en.wikipedia.org/wiki/Birthday_paradox .
# 
# 1. If there are 23 students in your class, what are the chances that two of you 
# have the same birthday? You can estimate this probability by generating random
# samples of 23 birthdays and checking for matches.
# 
# Hint: you can generate random birthdays with the randint function in the 
# random module.
#

import random


def has_duplicates(t):
    """Returns True if any element appears more than once in a sequence.

    t: list

    returns: bool
    """
    # make a copy of t to avoid modifying the parameter
    s = t[:]
    s.sort()

    # check for adjacent elements that are equal
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False


def random_bdays(n):
    """Returns a list of integers between 1 and 365, with length n.

    n: int

    returns: list of int
    """
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


def count_matches(num_students, num_simulations):
    """Generates a sample of birthdays and counts duplicates.

    num_students: how many students in the group
    num_samples: how many groups to simulate

    returns: int
    """
    count = 0
    for i in range(num_simulations):
        t = random_bdays(num_students)
        if has_duplicates(t):
            count += 1
    return count



"""Runs the birthday simulation and prints the number of matches."""
num_students = 23
num_simulations = 1000
answer = count_matches(num_students, num_simulations)