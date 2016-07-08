#!/usr/bin/env python3
# A script to capture and count instances of job titles in sample data.
# Next step is to find names of individuals holding those jobs.

import os, logging, re, pprint, datetime
logging.basicConfig(filename='../../sgmTidy-log-{::%Y%m%d-%H%M}.txt'.format(datetime.datetime.now()), level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def get_datafile():
    while True:
        try:
            datafile = input('Enter full path to data file: ')
            if os.path.isfile(datafile):
                return datafile
                break
            else:
                print('Check file exists in that location and try again.')
        except Exception as e:
            print('Something went wrong: {}'.format(str(e)))
            logging.critical('Exception: {}'.format(str(e)))

datafile = open(get_datafile())
logging.debug('opened {} as datafile'.format(datafile))

jobtitles = {}
jtregex = re.compile(r'<job>(.*?)</job>')

for i, line in enumerate(datafile):
    result = jtregex.findall(line)
    for item in result:
        if item not in jobtitles:
            jobtitles.setdefault(item, 0)
        jobtitles[item] += 1
    logging.debug('jtregex on line {0}'.format(i + 1)

# TODO: capture names matching each job titles

jtitles = list(jobtitles.keys()) # so that order becomes fixed
jholders = []

for j, line in enumerate(datafile):
    for k in titles:
        jhregex = re.compile(r'<job>{}</job><name>(.*?)</name>'.format(re.escape(k)))
        logging.debug('jhregex set to: {}'.format(jhregex))
        result = jhregex.findall(line)
        logging.debug('result: {}'.format(result))
        jholders += result
    logging.debug('jhregex loop on line {0}'.format(j + 1))

# end TODO for capturing names

with open('../../jobScraper-{:%Y%m%d-%H%M}.txt'.format(datetime.datetime.now()), 'w') as logfile:
    # pprint.pprint(jobtitles, logfile) # commented out while I debug TODO section
    pprint.pprint(holders, logfile)

datafile.close()
logfile.close()
print('Script ended')
logging.debug('End of program')
