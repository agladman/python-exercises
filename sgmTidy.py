#!/usr/bin/env python3
# sgmTidy.py cleans up raw sgml files ready for further analysis

# raising Exception and I don't know why yet

import re

def get_input_file():
    while True:
        try:
            input_file = input('Enter full path to input file: ')
            if os.path.isfile(input_file):
                return input_file
                break
            else:
                print('Gah! Check file exists in that location and try again.')
        except Exception as e:
            print('Something went wrong.')

with open(get_input_file()) as input_file:

    re.sub(r'>\s<', r'><', input_file)
    re.sub(r'\n', '', input_file)
    re.sub(r'(<[second|prim]ary)', r'\n\1', input_file)

close(input_file)
print('Script sgmTidy.py complete')
