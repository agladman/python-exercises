#! /usr/bin/env python3

import re

matches = []

myRegex = re.compile(r'[A-Za-z0-9 \-?]+\.pdf\:\d{1,4}\:')

inputfile = '/Users/anthonygladman/Dropbox/python_exercises/log.txt'

for line in inputfile:
    check = myRegex.search(line)
    if check.group(0) != None and check.group(0) not in matches:
        matches = matches + check.group(0)

print('Results found: %s') % (str(len(matches)))

# if len(matches) != 0:
#    for i in range(len(matches)):
#        print(matches[i])

"""Traceback (most recent call last):
  File "/Users/anthonygladman/Dropbox/python_exercises/listLines.py", line 13, in <module>
    if check.group(0) != None and check.group(0) not in matches:
AttributeError: 'NoneType' object has no attribute 'group'"""
