#!/usr/bin/env Python3

"""Write a program that given a text file will create a new text file in
    which all the lines from the original file are numbered from 1 to n
    (where n is the number of lines in the file).
    """

import os

while True:
    ui = input('Enter a filename: ')
    if os.path.isfile(ui):
        filename = ui
        break
    else:
        print('File not found.')

with open(filename, 'r') as f:
    text = f.readlines()

output_filename = 'numbered-{0}'.format(os.path.basename(filename))

output = ''
for i, line in enumerate(text):
    output += '{0}:\t{1}'.format(i + 1, line)

with open(output_filename, 'a') as f:
    f.write(output)
