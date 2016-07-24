#!/usr/bin/env Python 3

"""Coin Flip Simulation - Write some code that simulates flipping a
    single coin however many times the user decides. The code should
    record the outcomes and count the number of tails and heads.
    """

from random import choice


def flip():
    coin = ['heads', 'tails']
    return choice(coin)

results = []
hsum = 0
tsum = 0

while True:
    try:
        ui = int(input('How many times do you want to flip the coin? '))
        if ui:
            end = ui
            break
    except TypeError as e:
        print(e)
        pass

for i in range(end):
    results.append(flip())

for item in results:
    if item == 'heads':
        hsum += 1

tsum = len(results) - hsum

print('Coin came up heads {0} times and tails {1} times.'.format(hsum, tsum))
# print('\nDetailed results were: ')
# for i, item in enumerate(results):
#     print('{0}: {1}'.format(i + 1, item))
