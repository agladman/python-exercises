#!/usr/bin/env python3


""" p59, chapter 4, exercise 4.2: write out a recursive function to count the number of items in a list."""


def count(my_list):
	if my_list == []:
		return 0
	else:
		return 1 + count(my_list[1:])


