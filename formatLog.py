#!/usr/bin/env python3
# take a log from omnisearch.sh and format it to be read in page order

import sys, os, re, logging, datetime

logging.basicConfig(filename='formatLog-{:%Y%m%d-%H%M}-log.txt'.format(datetime.datetime.now()), level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
logging.disable(logging.CRITICAL) # comment out this line to enable logging again

# filepath to log is passed as sys arg; if not script asks for it
if len(sys.argv) > 1:
    filepath = ' '.join(sys.argv[1:])
else:
    while True:
        try:
            ui = input('Enter full path to log file: ')
            if os.path.isfile(ui):
                filepath = ui
                break
            else:
                print('Check file exists in that location and try again.')
        except Exception as e:
            print('Something went wrong: {}'.format(str(e)))
            logging.critical('Exception: {}'.format(str(e)))

# setting input
cleanpath = os.path.abspath(filepath)
input_file = open(cleanpath, 'r')
logging.debug('opened {} as input file'.format(cleanpath))
logdata = input_file.readlines()

# setting output
stripname = os.path.basename(cleanpath.strip('.txt'))
logging.debug('stripname: {}'.format(stripname))
output_file = open('{}/{}-formatted-{:%Y%m%d-%H%M}.txt'.format(os.path.dirname(cleanpath), stripname, datetime.datetime.now()), 'a')
logging.debug('output file: {}'.format(output_file))

pnum_regex = re.compile(r'^(\d{1,4}\:)(.*)$')

pattern = ''
pattern_regex = re.compile(r'^§\d{,2}/\d{,2}\:(.*)$')

output_data = []

for line in logdata:
    p = re.match(pattern_regex, line)
    n = re.match(pnum_regex, line)
    if p:
        pattern = p.group(1).strip()
        logging.debug('pattern changed to: {}'.format(pattern))
    elif n:
        # append leading zeros
        num = n.group(1)
        while len(num) < 5:
            num = '0{}'.format(num)

        result = '{}{}:{}'.format(num, pattern, n.group(2))
        # logging.debug('result: {}'.format(result))

        output_data.append(result)

    else:
        continue

# sort into page number order and write to the output file
output_data.sort()
for item in output_data:
    output_file.write('{}\n'.format(item))

logging.debug('End of program')
