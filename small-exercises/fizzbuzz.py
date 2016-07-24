#!/usr/bin/env Python3

"""Fizz Buzz - Write a program that prints the numbers from 1 to 100.
    But for multiples of three print “Fizz” instead of the number and
    for the multiples of five print “Buzz”. For numbers which are
    multiples of both three and five print “FizzBuzz”.
    """


def check_for_fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz'
    elif i % 3 == 0 and i % 5 != 0:
        return 'Fizz'
    elif i % 5 == 0 and i % 3 != 0:
        return 'Buzz'
    else:
        return str(i)

for i in range(1, 100):
    print(check_for_fizzbuzz(i))
