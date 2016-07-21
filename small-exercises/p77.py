"""This script runs the collatz sequence on a number until a value of 1 is returned. See Automate The Boring Stuff With Python, 2nd edition, page 77."""

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

print('Enter number: ')

try:
    value = int(input())
except ValueError:
    print('You must enter a number')

while value != 1:
    value = collatz(value)
