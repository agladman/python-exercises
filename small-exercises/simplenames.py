#!/usr/bin/env Python3


from random import choice


firstnames = [
    'Alfie',
    'Anna',
    'Bob',
    'Bobbetta',
    'Callum',
    'Claire']

lastnames = [
    'Daveson',
    'Etterson',
    'Fishbone',
    'Gonglehoops',
    'Herpy-Boo',
    'Inkysplot']

name = choice(firstnames) + ' ' + choice(lastnames)

print("I have compiled a random name for you: {}. Isn't that great?".format(name))
