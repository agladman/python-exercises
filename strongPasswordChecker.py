#!/usr/bin/env python3
# exercise from p171 of ATBS

"""Strong Password Detection
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is
at least eight characters long, contains both uppercase and lowercase
characters, and has at least one digit. You may need to test the string against
multiple regex patterns to validate its strength."""

import re

def checkpw(text):
    pwChaRegex = re.compile(r'[A-Z]+[a-z]+\d+')
    pwLenRegex = re.compile(r'.{8,}')
    if pwChaRegex.search(text) and pwLenRegex.search(text):
        print('Passvord STRONK!')
    else:
        print('You need a better password.')

def getpw():
    return str(input('Enter a password to check: '))

checkpw(getpw())
