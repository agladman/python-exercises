#!/usr/bin/env python3


"""Counts frequency of words in a text."""


import os.path
import string


def get_filename():
    while True:
        ui = input('Enter filename: ').strip()
        if os.path.isfile(ui):
            return ui
        else:
            print('File not found, please try again.')


def word_freq_dict(sometext):
    word_dict = {}
    for line in sometext:
        linewords = line.split()
        for word in linewords:
            word = clean_word(word)
            if word not in word_dict:
                word_dict.setdefault(word, 0)
            word_dict[word] += 1
    return word_dict


def clean_word(somestring):
    """Cleans punctuation from string and returns it as lower case."""
    somestring = somestring.strip('“')  # not part of string.punctuation
    return somestring.strip(string.punctuation).lower()


def dict_to_list(somedict):
    """Takes a dict of tuples and returns it as a list, sorted on the first element in each tuple."""
    output = [(k, v) for k, v in somedict.items()]
    return sorted(output, key=lambda item: item[1], reverse=True)


def make_table(somelist):
    while somelist:
        for idx in range(5):
            try:
                display(somelist.pop(0))
            except IndexError:  # if list finishes partway through a line
                pass
        print('\n')


def display(sometuple):
    k, v = sometuple
    if k == '\n':
        k = '\\n'
    if k == '\t':
        k = '\\t'
    v = str(v).rjust(5, ' ')
    print(f'\t\'{k}\': {v}', end='')


def main():
    filename = get_filename()

    with open(filename, 'r') as f:
        text = f.readlines()

    data = word_freq_dict(text)
    datalist = dict_to_list(data)
    for thing in datalist:
        if 251 > thing[1] > 99:
            display(thing)
            print('\n')


if __name__ == '__main__':
    main()