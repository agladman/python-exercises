#!/usr/bin/env Python3

"""Write a procedure char_freq_table() that, when run in a terminal,
    accepts a file name from the user, builds a frequency listing of the
    characters contained in the file, and prints a sorted and nicely
    formatted character frequency table to the screen.
    """

import os.path


def get_filename():
    while True:
        ui = input('Enter filename: ').strip()
        if os.path.isfile(ui):
            return ui
        else:
            print('File not found, please try again.')


def char_freq_dict(text):
    chars = {}
    for line in text:
        for ch in line:
            if ch not in chars:
                chars.setdefault(ch, 0)
            chars[ch] += 1
    return chars


def dict_to_list(somedict):
    """Takes a dict of tuples and returns it as a list, sorted on the first element in each tuple."""
    chars = [(k, v) for k, v in somedict.items()]
    return sorted(chars, key=lambda char: char[0])


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
        text = f.read()

    data = char_freq_dict(text)
    make_table(dict_to_list(data))


if __name__ == '__main__':
    main()
