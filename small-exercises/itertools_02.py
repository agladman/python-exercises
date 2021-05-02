#!/usr/bin/env python3

"""more pissing about in order to learn itertools"""

from itertools import permutations, zip_longest, cycle, repeat

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

def try_perm():
    p2 = permutations(names, 2)
    p3 = permutations(names, 3)
    p4 = permutations(names, 4)
    print(f"there are {len(names)} names")
    print(f"there are {len(list(p2))} permutations for pairs of names")
    print(f"there are {len(list(p3))} permutations for trios of names")
    print(f"there are {len(list(p4))} permutations for fours of names")
    print("the increase is factoral, so permutations is O(n!), which is slooooow...")
    print("the permutations objects are generaetors, they are stateful, and are now exhausted")
    print(f"Calling next() on p2 now will raise StopIteration.")
    print("remaking a list of p2...")
    x = list(permutations(names, 2))
    for i, p in enumerate(x):
        print(i + 1, p)

def try_zl():
    z = zip_longest(names, workers)
    print("dicking about with zip_longest")
    print(f"{names=}")
    print(f"{workers=}")
    print(f"zip_longest names, workers: {z}")
    for i, x in enumerate(z):
        print(i, x)
    names.extend(["alice", "graham", "peter", "grace"])
    print(f"names has been extended and now has {len(names)} names")
    print(f"workers has {len(workers)} names")
    print("zip_longest no fill value given")
    zz = zip_longest(names, workers)
    for i, x in enumerate(zz):
        print(i, x)
    print("zip_longest, fill value given")
    zf = zip_longest(names, workers, fillvalue="-fill-")
    for i, x in enumerate(zf):
        print(i, x)
    fill = cycle("ABC")
    print("zip_longest, fill value given using cycle")
    zf = zip_longest(names, workers, fillvalue=next(fill))
    for i, x in enumerate(zf):
        print(i, x)
    print("doesn't work, using next(fill) just evals once when zip_longest first called")

if __name__ == '__main__':
    try_zl()
