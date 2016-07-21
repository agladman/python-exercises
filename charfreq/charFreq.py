#!/usr/bin/env Python3

"""Write a procedure char_freq_table() that, when run in a terminal,
    accepts a file name from the user, builds a frequency listing of the
    characters contained in the file, and prints a sorted and nicely
    formatted character frequency table to the screen.
    """

import os
import pprint


def char_freq_table(text):
    chars = {}
    for line in text:
        for ch in line:
            if ch not in chars:
                chars.setdefault(ch, 0)
        chars[ch] += 1
    output = pprint.pprint(chars)
    return output

while True:
    ui = input('Enter filename: ').strip()
    if os.path.isfile(ui):
        filename = ui
        break
    else:
        print('File not found, please try again.')

with open(filename, 'r') as f:
    text = f.read()

char_freq_table(text)
