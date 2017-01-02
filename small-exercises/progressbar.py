#!/usr/bin/env Python3

"""Should produce a progress count that updates in place rather than over
    multiple lines."""


import sys


completion = 0
while completion < 100:
    sys.stdout.write('This is a progress bar: {:.0f}% \r'.format(completion))
    sys.stdout.flush()
    completion += 1
