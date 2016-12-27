#!/usr/bin/env Python3

username1 = input("Hello you please enter a username! ")
password1 = input("Now can you enter a password? Try to make it a strong one, ")

enteredpassword = ''
while enteredpassword != password1:
    enteredpassword = input("Please try again, {}: ".format(username1))
    if enteredpassword == password1:
        print("YAY! corrrect ")
        break
    else:
        print("Bum. Not correct.")
        continue
