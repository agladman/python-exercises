#!/usr/bin/env python3

"""
Calculates reading time based on average pace of 130 words per minute.
"""


import sys, time

def mpace(p):
    if type(p) == int and p > 0:
        return p
    else:
        match p:
            case "slow":
                return 100
            case "average":
                return 130
            case "fast":
                return 160
            case _:
                raise ValueError

def main():

    words = None
    pace = 130

    # capture words and pace from sys args if passed
    if len(sys.argv) == 2:
        words = int(sys.argv[1])
    elif len(sys.argv) > 2:
        words = int(sys.argv[1])
        p = sys.argv[2]
        if p.isnumeric():
            p = int(p)
        pace = mpace(p)

    # get words from user if still needed, pace stays as default
    if words is None:
        words = int(input("Enter wordcount: "))

    # perform the calculation
    sec = words/pace * 60
    ty_res = time.gmtime(sec)
    res = time.strftime("%Hh:%Mm:%Ss", ty_res)
    print(f"Reading time: {res}")

if __name__ == '__main__':
    main()
