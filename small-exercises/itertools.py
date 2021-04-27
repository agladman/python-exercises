#!/usr/bin/env python3

"""
Pissing about in order to learn itertools
"""

from itertools import product
import timeit


names = ['marcus', 'bill', 'don', 'bob', 'linda', 'lorraine', 'gloria']

jobs = {
    'fred': 'paranormal investigator',
    'bill': 'burger chef',
    'louise': 'trainee ghost',
    'jeff': 'unemployed',
    'linda': 'meter maid',
    'gloria': 'fishwife',
    'gonzo': 'ace reporter'
    }

workers = set(jobs.keys())

def use_product():
    results = []
    for n, w in product(names, workers):
        if n == w:
            results.append(f'{n} is a {jobs[n]}')
    return results

def use_pop_and_loop():
    checklist = [n for n in names]  # copy list so original is not effected
    results = []
    while checklist:
        n = checklist.pop()
        for w in workers:
            if n == w:
                results.append(f'{n} is a {jobs[n]}')
    return results

def use_get():
    return [f'{n} is a {jobs.get(n)}' for n in names if jobs.get(n)]

prod = min(timeit.Timer(use_product).repeat(10, 1000))
poploop = min(timeit.Timer(use_pop_and_loop).repeat(10, 1000))
get = min(timeit.Timer(use_get).repeat(10, 1000))

print(f'{use_product()=}')
print(f'{use_pop_and_loop()=}')
print(f'{use_get()=}')

print(f'with use_product:\t{prod:.8f} seconds')
print(f'with use_pop_and_loop:\t{poploop:.8f} seconds')
print(f'with use_get:\t\t{get:.8f} seconds')
