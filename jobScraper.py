#!/usr/bin/env python3
# A script to capture and count instances of job titles in sample data.
# Next being to find names of individuals holding those jobs.

import os, re, pprint

def get_datafile():
    while True:
        try:
            datafile = input('Enter full path to data file: ')
            if os.path.isfile(datafile):
                return datafile
                break
            else:
                print('Gah! Check file exists in that location and try again.')
        except Exception as e:
            print('Something went wrong.')

datafile = open(get_datafile())

# with open('filename.ext') as input_file:

jobtitles = {}
jtregex = re.compile(r'>(.*?)</job>')

for line in datafile:
    result = jtregex.findall(line)
    for item in result:
        if item not in jobtitles:
            jobtitles.setdefault(item, 0)
        jobtitles[item] += 1

# TODO: capture names matching each job titles

"""Alternatively get the user to indicate which job titles are of
interest and capture names that match the selection."""

"""Need a regex to find similar patterns following each k in jobtitles.
Resulting lists from re.findall stored in a list of lists? How to match to key?
Some sort of index number taken from i as it loops through?
And how to print it all out once it's done?"""

with open('../../jobScraper-log.txt', 'w') as logfile:
    pprint.pprint(jobtitles, logfile)

datafile.close()
logfile.close()
print('Script ended')
