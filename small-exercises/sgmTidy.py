#!/usr/bin/env python3
# sgmTidy.py cleans up raw sgml files ready for further analysis

import logging, re, os

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def multiple_replace(dict, text):
    # from http://stackoverflow.com/a/15175239/6409460
    # Create a regular expression  from the dictionary keys
    logging.debug('creating regex')
    regex = re.compile('({})'.format('|'.join(map(re.escape, dict.keys()))))

    # For each match, look-up corresponding value in dictionary
    logging.debug('looking up match in dictionary')
    return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)

patterns = {'>\s<': '><', '\n': '', '(<[second|prim]ary)': '\n\1'}

if __name__ == '__main__':

    def get_file_path():
        while True:
            try:
                file_path = input('Enter filepath: ')
                if os.path.isfile(file_path):
                    return file_path
                    break
                else:
                    print('Check file exists in that location and try again.')
            except Exception as e:
                print('Something went wrong: {}'.format(str(e)))

    with open(get_file_path(), 'r+') as datafile:
        logging.debug('opening datafile')
        output = multiple_replace(patterns, datafile.read())
        logging.debug('fetching output')
        datafile.write(output)
        logging.debug('writing output')

    datafile.close()
    print('Script sgmTidy.py complete')
    logging.debug('End of program')
