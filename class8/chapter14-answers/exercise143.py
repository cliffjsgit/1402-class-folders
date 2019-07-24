#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 14.3
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "find_duplicates" should take a string reprensentation of a
# directory to search, find all the duplicates, and returns a list of complete 
# paths for any duplicates in the form of tuples.
# 
# In a large collection of MP3 files, there may be more than one copy of the 
# same song, stored in different directories or with different file names. The 
# goal of this exercise is to search for duplicates.
# 
# 1. Write a function named "find_duplicates" that takes a string 
# reprensentation of a directory to search, searches that directory and 
# all of its subdirectories, recursively, and returns a list of complete 
# paths for any duplicates in the form of tuples.
# 
# 2. To recognize duplicates, you can use md5sum to compute a "checksum" for 
# each files. If two files have the same checksum, they probably have the same 
# contents.
#
import os


def walk(dirname):
    """Finds the names of all files in dirname and its subdirectories.

    dirname: string name of directory
    """
    names = []
    if '__pycache__' in dirname:
        return names

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names


def compute_checksum(filename):
    """Computes the MD5 checksum of the contents of a file.

    filename: string
    """
    cmd = 'md5sum ' + filename
    return pipe(cmd)


def check_diff(name1, name2):
    """Computes the difference between the contents of two files.

    name1, name2: string filenames
    """
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)


def pipe(cmd):
    """Runs a command in a subprocess.

    cmd: string Unix command

    Returns (res, stat), the output of the subprocess and the exit status.
    """
    # Note: os.popen is deprecated
    # now, which means we are supposed to stop using it and start using
    # the subprocess module.  But for simple cases, I find
    # subprocess more complicated than necessary.  So I am going
    # to keep using os.popen until they take it away.

    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat


def compute_checksums(dirname, suffix):
    """Computes checksums for all files with the given suffix.

    dirname: string name of directory to search
    suffix: string suffix to match

    Returns: map from checksum to list of files with that checksum
    """
    names = walk(dirname)

    d = {}
    for name in names:
        if name.endswith(suffix):
            res, stat = compute_checksum(name)
            checksum, _ = res.split()

            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]

    return d


def check_pairs(names):
    """Checks whether any in a list of files differs from the others.

    names: list of string filenames
    """
    for name1 in names:
        for name2 in names:
            if name1 < name2:
                res, stat = check_diff(name1, name2)
                if res:
                    return False
    return True


def print_duplicates(d):
    """Checks for duplicate files.

    Reports any files with the same checksum and checks whether they
    are, in fact, identical.

    d: map from checksum to list of files with that checksum
    """
    for key, names in d.items():
        if len(names) > 1:
            print('The following files have the same checksum:')
            for name in names:
                print(name)

            if check_pairs(names):
                print('And they are identical.')


if __name__ == '__main__':
    d = compute_checksums(dirname='.', suffix='.py')
    print_duplicates(d)