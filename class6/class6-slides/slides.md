---
title: 'Class 6: Chapter 12: Tuples'
separator: '\-\-\-\-\-'
verticalSeparator: '\+\+\+\+\+'
theme: 'moon'
revealOptions:
    transition: 'fade'
---

### ITSE-1402 Intermediate Python
<span style="font-family:Helvetica Neue; font-weight:bold; color:#e49436">Class 6: Chapter 12: Tuples</span>
<br /><br />
##### [https://coder.run/1402-class6](https://coder.run/1402-class6)

-----

##### Chapter 12: Tuples

+++++

[https://coder.run/1402-chap12](https://coder.run/1402-chap12)

+++++

#### Testing Knowledge!

- What are two ways to create a dictionary?
- What data types can a dictionary key be?
- What data types can the object to a dictionary key be?
- What are the 3 ways we discussed to get a object from a dictionary and what are their differences?
- When you interate through a dictionary, what are you receiving back?

+++++

##### Tuples

Tuples are essentially lists and operate the same in many ways as a list, however they are immutable. Meaning they cannot be modified.

+++++

Empty tuples can be created in two ways:
- using the built-in function tuple
- using parentheses

```python
myTuple = tuple()   # Empty tuple using built-in
myTuple2 = ()      # Empty tuple using parentheses
```

+++++

You can also use the built-in function "tuple" to make a tuple out of an interable object:

```python
t = tuple('hello')
# t = ('h','e','l','l','o')
```

+++++

When defining a tuple with predefined values, it can be done two different ways; both valid:

```python
tuple1 = 1,2,3,4,5,6,7
tuple2 = (1,2,3,4,5,6,7)
```

Note:
Parentheses around the tuple are optional, however it makes it more easily identifiable.

+++++

Most list operators also work on tuples. The bracket operator indexes an element:

```python
t = ('a','b','c','d','e')
# t[0] = 'a'
```

And the slice operator selects a range of elements.

```python
t[1:3]
# ('b','c')
```
+++++

But if you try to modify one of the elements of the tuple, you get an error:

```python
t[0] = 'A'
# TypeError: object doesn't support item assignment
```

Because tuples are immutable,  you can’t modify the elements.  But you can replace one tuple with another:

```python
t = ('A',) + t[1:]
# t = ('A','b','c','d','e')
```

+++++

Relational operators work with tuples as well as lists. When comparing Python begins with the first element from each sequence. If they are equal, it goes on to the next elements until it differs.  Elements moving forward are not compared.

```python
(0,1,2) < (0,3,4)
#True
(0,1,2000000) < (0,3,4)
#True
```

+++++

You may find that sometimes you need to swap two variables or assign multiple variables at once. You could do it like so:

```python
a = 1
b = 2
temp = a
a = b
b = temp
```

This is not ideal though.

+++++

Tuple assignment can make this much better:

```python
a,b = 1,2
a,b = b,a
# a = 2
# b = 1
```

Note: 
The left side is a tuple of variables; the right side is a tuple of expressions. Each value is assigned to its respective variable.  All the expressions on the right side are evaluated before any of the assignments. 

+++++

The number of variables on each side of the tuple assignment must be the same or you will get an error:

```python
a,b = 1,2,3
# ValueError: too many values to unpack
```

+++++

This right portion can be any type of sequence. An example of this would be an email address:

```python
email = myemail@domain.com
user,domain = email.split('@')
# user = myemail
# domain = domain.com
```

+++++

When working with functions, there can only be one value returned. This changes when you introduce tuples. This can be seen with the built-in function "divmod".

```python
t = divmod(7,3)
# t = (2,1)
```

You then can use tuple assignment to store the values

```python
quot,rem = divmod(7,3)
# quot = 2
# rem = 1
```

+++++

The way this concept would look in a function is like so:

```python
def min_max(t):
    return min(t),max(t)
```

+++++

<pre class="stretch"><code class="python" data-trim data-noescape>
#!/usr/bin/env python3

# Exercise 12.1
#
# 1. Write a function called "most_frequent" that takes a string and returns 
# a list of letters in decreasing order of frequency. 
#
# Find text samples from several different languages and see how letter 
# frequency varies between languages. Compare your results with the tables at:
# http://en.wikipedia.org/wiki/Letter_frequencies
</code></pre>

+++++

We've seen that tuples can help with returning elements, but they can also help with intaking them also:

```python
def print_all(*args)
    print(args)
    
print_all(1,2.0,'3')
# (1,2.0,'3')
```

Note: 
When you add an argument to a function definition with a * preceding the word, it takes a variable number of arguments.
This can be combined with other arguments and anything after the static number is taken in as "args", a tuple
"args" is the conventional word to use there, but you can use any word that would work as a variable there.

+++++

This same concept can be used on the other side of the function as well. This is called "scatter".

```python
t = (7,3)
divmod(t)
# TypeError: divmod expected 2 arguments, got 1

divmod(*t)
# (2,1)
```

Note:
Divmod normally requires two variables, but scatter will separate the tuple into individual values

+++++

Depending on the function you run, some will take a variable number of arguments, but others will not. Refer to the documentation of the function to verify.

```python
max(1,2,3)
# 3

min(1,2,3)
# 1

sum(1,2,3)
# TypeError: sum expected at most 2 arguments, got 3
```

Note:
Max and Min are examples of functions that take a variable number of arguments. Sum is one that does not.

+++++

```python
Write a function called "sumall" that
takes any number of arguments and 
returns their sum.
```

Note:
Not an official exercise, but let's think it through.

+++++

zip is a built-in function that uses tuples to create pairs of objects between two or more iterables

```python
s='abc'
t=[0,1,2]
zip(s,t)
<zip object at 0x7f7d0a9e7c48>
```

Note:
The result is a zip object, not an actual list. You cannot reference a zip in it's native form with an index.

+++++

Assuming you want to see the objects in the zip, this would be one way to do that:

```python
for pair in zip(s,t):
    print(pair)

#('a',0)
#('b',1)
#('c',2)
```

+++++

If you would like to work with a zip as a list, it is rather simple to do:

```python
list(zip(s,t))
#[('a',0),('b',1),('c',2)]
```

+++++

Assuming you have two iterables with different lengths that you zip, it will be the lenght of the shortest interable and drop the rest:

```python
list(zip('Anne','Elk'))
[('A','E'),('n','l'),('n','k')]
```

+++++

Dictionaries have a method called items that returns a sequence of tuples where each is the key,value pair from the dictionary.

```python
d = {'a':0, 'b':1, 'c':2}
t = d.items()
# t = dict_items([('c', 2), ('a', 0), ('b', 1)])
```

The result is a dict_items object, which is an iterator that iterates the key-value pairs. 

+++++

You can interate through d.items() like so:

```python
for key, value in d.items():
    print(key, value)
# c 2
# a 0
# b 1
```

+++++

You can also use a list of tuples to initialize a new dictionary:

```python
t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)
# d = {'a': 0, 'c': 2, 'b': 1}
```

+++++

Along the same lines, you can also use zip to make a dictionary:

```python
d = dict(zip('abc', range(3)))
# d = {'a': 0, 'c': 2, 'b': 1}
```

Note: 
There is also a dictionary method update takes a list of tuples and adds them, as key-value pairs, to an existing dictionary.

+++++

It is common to use tuples as keys in dictionaries (primarily because you can’t use lists).

```python
directory["Doe", "John"] = "+1 111-111-1111"

for last, first in directory:
    print(first, last, directory[last,first])
```

Note: 
For example, a telephone directory might map from last-name, first-name pairs to telephone numbers. Assuming that we have defined last, first and number, we could write:

+++++

<pre class="stretch"><code class="python" data-trim data-noescape>
#!/usr/bin/env python3

# Exercise 12.2
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "anagram_finder" should return a list of of all the sets of 
# words that are anagrams.
# - Function "anagram_finder2" should return a list of of all the sets of 
# words that are anagrams in ascencing order by number of anagrams. 
# - Function "anagram_bingo" should return a list containing the collection 
# of 8 letters that forms the most possible bingos
#
# 1. Write a function named "anagram_finder" that reads a word list 
# from a file and returns a list of all the sets of words that are anagrams.
# 
# Here is an example of what the output might look like:
# [
#   ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled'],
#   ['retainers', 'ternaries'],
#   ['generating', 'greatening'],
#   ['resmelts', 'smelters', 'termless']
# ]
#
# Hint: you might want to build a dictionary that maps from a collection of 
# letters to a list of words that can be spelled with those letters. The 
# question is, how can you represent the collection of letters in a way that 
# can be used as a key?
#
#
# 2. Create a modified function of the above named "anagram_finder2" so that it 
# prints the longest list of anagrams first, followed by the second longest, 
# and so on.
# 
#
# 3. In Scrabble a "bingo" is when you play all seven tiles in your rack, along 
# with a letter on the board, to form an eight-letter word. Write a function
# named "anagram_bingo" that returns a list containing the collection of 8
# letters that forms the most possible bingos. Hint: there are seven.
# 
</code></pre>

+++++

Exercise 12.3 and 12.4 are homework. You may do a CodeFights Challenge for extra credit