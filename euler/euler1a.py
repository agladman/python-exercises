#!/usr/bin/env Python3

def check_number(i):
    if i % 3 == 0:
        return True
    elif i % 5 == 0:
        return True
    else:
        return False

sum = 0
for i in range(1000):
    if check_number(i):
        sum += i

print(sum)
