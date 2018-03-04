#!/usr/bin/env python3

"""
Happy Numbers
A happy number is defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in
a cycle which does not include 1. Those numbers for which this process ends in 1 are happy
numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output
here. Find the first eight happy numbers.
"""


def square_digit_sum(num):
    return sum(int(n)**2 for n in str(num))


def is_happy(num):
    seen = set()
    while num > 1:
        if num in seen:
            return False
        seen.add(num)
        num = square_digit_sum(num)
    return True


happy_numbers = [num for num in range(1000) if is_happy(num)]
