#!/usr/bin/env python3


""" p59, chapter 4 exercise 4.3, write a recursive function to find the maximum number in a list."""


def getmax(mylist):
	if len(mylist) == 2:
		return mylist[0] if mylist[0] > mylist[1] else mylist[1]
	submax = getmax(mylist[1:])
	return mylist[0] if mylist[0] > submax else submax

