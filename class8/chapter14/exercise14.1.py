#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 14.1\n")
#
# Question 1
# 1. Write a function called sed that takes as arguments a pattern string, a
# replacement string, and two filenames; it should read the first file and write
# the contents into the second file (creating it if necessary). If the pattern
# string appears anywhere in the file, it should be replaced with the
# replacement string.
# 
# If an error occurs while opening, reading, writing or closing files, your
# program should catch the exception, print an error message, and exit.
#
def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.

    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    fin = open(source, 'r')
    fout = open(dest, 'w')

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)

    fin.close()
    fout.close()


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sed_tester.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


if __name__ == '__main__':
    main()