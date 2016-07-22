#!/usr/bin/env Python 3

"""Write a program that will calculate the average word length of a text
    stored in a file (i.e the sum of all the lengths of the word tokens
    in the text, divided by the number of word tokens).
    """

import os

while True:
    ui = input('\nEnter a filename: ')
    if os.path.isfile(ui):
        filename = ui
        break
    else:
        print('File not found.')    

with open(filename, 'r') as f:
    text = f.read().split()

lengths = 0
count = 0

for word in text:
    lengths += len(word)
    count += 1

average_word_length = lengths / count

print('Average word length in {0} is {1}.\n'.format(filename, int(average_word_length)))
