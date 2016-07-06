#!/usr/bin/env python3

"""Regex Version of strip()
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to strip,
then whitespace characters will be removed from the beginning and end of the
string. Otherwise, the characters specified in the second argument to the
function will be removed from the string."""

import re

def regex_strip(my_text, chars=None):
    if not chars:
        x = r'\s'
    else:
        x = prep_for_regex(chars)
    return re.sub(r'^' + x + '*(.*?)' + x + '*$', r'\1', my_text, re.DOTALL)

def prep_for_regex(chars):
    needs_escape = set('.^$*+?{}[]\|()')
    for ch in chars:
        if ch in needs_escape:
            ch = '\\' + ch
    chars = '[' + chars + ']'
    return chars

def get_text():
    return str(input('Enter some text: '))

def get_chars():
    return str(input('What do you want to remove? (Leave blank for whitespace.) '))

print(regex_strip(get_text(), get_chars()))
