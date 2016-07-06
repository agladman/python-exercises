#!/usr/bin/env python3

"""Regex Version of strip()
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to strip,
then whitespace characters will be removed from the beginning and end of the
string. Otherwise, the characters specified in the second argument to the
function will be removed from the string."""

import re

def reStrip(s1, s2):
    if s2 == '': # no second argument passed
        stripRegex = re.compile(r'[^\s]*')
    else:
        x = '[^%s]*' % (s2) # could be improved by ignoring case?
        stripRegex = re.compile(x)
    # return output
    chars = stripRegex.findall(s1)
    printChars = ''
    for ch in chars:
        printChars += ch
    return printChars

def getText():
    return str(input('Enter some text: '))

def getStrip():
    return str(input('What do you want to remove? (Leave blank to strip just spaces.) '))

print(reStrip(getText(), getStrip()))
