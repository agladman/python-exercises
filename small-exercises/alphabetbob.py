#!/usr/bin/env Python3

"""
Write a program that asks the user for their name, and then prints out
their name with the first letter replaced by each letter of the alphabet
in turn, e.g. for 'Bob' it prints 'Aob', 'Bob', 'Cob', 'Dob' etc.
"""

alpha = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()

name = input('Please enter your name: ')

for letter in alpha:
    print(letter + name[1:])
