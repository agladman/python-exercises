#!/usr/bin/env python3
# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

def sum1(num):
    "a first attempt from long ago..."
    sum = 0
    for i in range(0, num):
        sum = sum + i
    sum = sum + num
    return sum

def sum2(num):
    "recursive attempt"
    if num == 0:
        return 0
    else:
        return num + sum2(num -1)

if __name__ == '__main__':
    num = int(input('Enter a number: '))
    print(f'sum1: {sum1(num)}')
    print(f'sum2: {sum2(num)}')
