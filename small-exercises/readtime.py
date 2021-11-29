#!/usr/bin/env python3

"""
Calculates reading time based on average pace of 130 words per minute.
"""


import sys, time

# slow = 100
norm = 130
# fast = 160

def calc(w, pace=norm):
    return w/pace * 60

def main():
    w = None
    if len(sys.argv) >= 2:
        w = int(sys.argv[1])
    if w is None:
        w = int(input("Enter wordcount: "))
    sec = calc(w)
    ty_res = time.gmtime(sec)
    res = time.strftime("%Hh:%Mm:%Ss", ty_res)
    print(f"Reading time: {res}")

if __name__ == '__main__':
    main()
