#!/usr/bin/env python3

"""A hapax legomenon (often abbreviated to hapax) is a word which occurs
    only once in either the written record of a language, the works of
    an author, or in a single text. Define a function that given the
    file name of a text will return all its hapaxes. Make sure your
    program ignores capitalization.
    """
import os

def hapax(filename):
    with open(filename) as f:
        text = f.read().split()

    words = {}
    for word in text:
        word = word.strip('.,!?').lower()
        if word not in words:
            words.setdefault(word, 0)
        words[word] += 1

    hapaxes = []

    for k, v in words.items():
        if v == 1:
            hapaxes.append(k)

    hapaxes.sort(key=str.lower)
    output = ''

    last = len(hapaxes) - 1

    for i, item in enumerate(hapaxes):
        if i == last:
            output += '{0}.'.format(item)
        else:
            output += '{0}, '.format(item)

    return output

while True:
    ui = input('Enter a filename: ')
    if os.path.isfile(ui):
        filename = ui
        break
    else:
        print('File not found.')

print('\nHapax legomena in {0}: {1}\n'.format(filename, hapax(filename)), end='')