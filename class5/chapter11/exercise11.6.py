#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 11.6\n")
#
# Question 1
# 1. Here's another Puzzler from Car Talk 
# (http://www.cartalk.com/content/puzzlers):
#
# This was sent in by a fellow named Dan O'Leary. He came upon a common
# one-syllable, five-letter word recently that has the following unique 
# property. When you remove the first letter, the remaining letters form a 
# homophone of the original word, that is a word that sounds exactly the same. 
# Replace the first letter, that is, put it back and remove the second letter 
# and the result is yet another homophone of the original word. And the question
# is, what's the word?
#
# Now I'm going to give you an example that doesn't work.  Let's look at the
# five-letter word, ‘wrack.'  W-R-A-C-K, you know like to ‘wrack with pain.'
# If I remove the first letter, I am left with a four-letter word, 'R-A-C-K.' 
# As in, ‘Holy cow, did you see the rack on that buck! It must have been a nine-
# pointer!' It's a perfect homophone. If you put the ‘w' back, and remove the 
# ‘r,' instead, you're left with the word, ‘wack,' which is a real word, it's 
# just not a homophone of the other two words.
#
# But there is, however, at least one word that Dan and we know of, which will 
# yield two homophones if you remove either of the first two letters to make 
# two, new four-letter words. The question is, what's the word?
# 
# You can use the dictionary from Exercise 11.1 to check whether a string is in
# the word list.
# 
# To check whether two words are homophones, you can use the CMU Pronouncing 
# Dictionary. You can download it from http://thinkpython2.com/code/c06d.txt 
# and you can also download http://thinkpython2.com/code/pronounce.py
# which provides a function named read_dictionary that reads the pronouncing
# dictionary and returns a Python dictionary that maps from each word to a string
# that describes its primary pronunciation.
# 
# Write a program that lists all the words that solve the Puzzler.
#
''' Create empty word dictionaries '''
word_dict = dict()
pron_dict = dict()

''' Creating the word dictionary '''
def create_word_dict():
    d = dict()
    fin = open("words.txt")

    for line in fin:
        d[line.strip()] = ""
    fin.close()
    
    return d

''' Find the new 4-letter words in the word dictionary '''
def find_word(word):
    if word in word_dict:
        return True
    return False

''' Creating the pronounciation dictionary '''
def read_dictionary(filename):
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

''' Check the pronounciation of new words '''
def check_proonounciation_match(word1, word2):
    # Not all new words are in the pronounciation dictionary
    if (word1 in pron_dict) and (word2 in pron_dict):
        #print(pron_dict[word1], pron_dict[word2])
        if pron_dict[word1] == pron_dict[word2]:
            return True
    return False
    
if __name__ == "__main__":
    # Build dictionaries
    word_dict = create_word_dict()
    pron_dict = read_dictionary("c06d.txt")
    
    # Need to find words that are 5 characters in length
    for next_word in word_dict:
        if len(next_word) == 5:
            # Make sure the new 4-letter words are in the word list
            if find_word(next_word[1:]) and find_word(next_word[:1]+next_word[2:]):
                # If valid words, check pronounciation
                if (check_proonounciation_match(next_word[1:], (next_word[:1]+next_word[2:]))):
                    # Print any words that match
                    print("5-letter word with matching 4-letter homophones when the first or second letter is removed")
                    print("Word: {0}\t 1st Letter Removed: {1}\t 2nd Letter Removed: {2}".\
                    format(next_word,next_word[1:], (next_word[:1]+next_word[2:])))
                    print()