#!/usr/bin/env python3

# this one's not from the book
# objecrtive: a recursive function to count the consonsants in a string

def count_consonants(string):
	"counts the number of consonsants in a string"
	consonsants = "bcdefghjklmnpqrstvwxyz"
	# base case
	if len(string) == 1:
		return 1 if string[0] in consonsants else 0
	# recursive case
	if len(string) > 1:
		c = 1 if string[0] in consonsants else 0
		return c + count_consonants(string[1:])
