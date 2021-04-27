#!/usr/bin/env python3

"""
A script to find the sum of all the multiples of 3 or 5 below 1000.
My intention is to use recursion to do this as effeciently as possible.
"""

def euler(num):
	"returns sum of all multiples of 3 or 5 below num"
	if num <= 0:
		return 0
	elif num % 3 == 0 or num % 5 == 0:
		return num + euler(num - 1)
	else:
		return euler(num - 1)

if __name__ == '__main__':
    print(euler(1000))
