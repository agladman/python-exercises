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

# run with the following... not great
# for i in range(1, 100):
#     print(check_for_fizzbuzz(i)
#
# let's try a better version...

def fizzbuzz(num):
    for n in range(1, num + 1):
        fizz = "fizz" if n % 3 == 0 else ''
        buzz = "buzz" if n % 5 == 0 else ''
        yield f"{fizz}{buzz}".capitalize() if fizz or buzz else n

def main():
    while True:
        try:
            num = int(input("Enter a number: "))
            if 0 < num < 100:
                break
            else:
                print("No one likes a smartarse...")
                continue
        except ValueError:
            print("That's not a number!")
            continue
    for n in fizzbuzz(num):
        print(n)

if __name__ == '__main__':
    main()
