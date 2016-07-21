#!/usr/bin/env python3
# A script to capture and count instances of job titles in sample data.
# Next step is to find names of individuals holding those jobs.

import os, logging, re, pprint, datetime
logging.basicConfig(filename='../../jobScraper-{:%Y%m%d-%H%M}-log.txt'.format(datetime.datetime.now()), level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

while True:
    try:
        ui = input('Enter full path to data file: ')
        if os.path.isfile(ui):
            datafile = open(ui, 'r')
            logging.debug('opened {} as datafile'.format(datafile))
            break
        else:
            print('Check file exists in that location and try again.')
    except Exception as e:
        print('Something went wrong: {}'.format(str(e)))
        logging.critical('Exception: {}'.format(str(e)))

all_lines = datafile.readlines()

jobtitles = {}
jtregex = re.compile(r'<job>(.*?)</job>')

result = jtregex.findall(all_lines)
for item in result:
    if item not in jobtitles:
        jobtitles.setdefault(item, 0)
    jobtitles[item] += 1
# logging.debug('jtregex run on line {0}'.format(i + 1))

# TODO: capture names matching each job titles

jtitles = list(jobtitles.keys()) # so that order becomes fixed
logging.debug('jtitles: {}'.format(jtitles))
jholders = []

for k in jtitles:
    jhregex = re.compile(r'<job>{}</job><name>(.*?)</name>'.format(re.escape(k)))
    if j <= 1: # stops log from getting too big
        logging.debug('jhregex set to: {}'.format(jhregex))
    result = jhregex.findall(all_lines)
    if j <= 1: # stops log from getting too big
        logging.debug('result: {}'.format(result))
    jholders += result

logging.debug('jholders: {}'.format(jholders))
holders = {zip(jtitles, jholders)}

# end TODO for capturing names

with open('../../jobScraper-{:%Y%m%d-%H%M}.txt'.format(datetime.datetime.now()), 'w') as output_file:
    # pprint.pprint(jobtitles, output_file) # commented out while I debug TODO section
    pprint.pprint(holders, output_file)

datafile.close()
output_file.close()
print('Script ended')
logging.debug('End of program')
