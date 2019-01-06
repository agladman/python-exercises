#!/usr/bin/env python3


def fact(x):
	if x == 1:
		return 1
	else:
		return x * fact(x - 1)


def addfact(x):
	if x == 1:
		return 1
	else:
		return x + addfact(x - 1)


def subfact(x):
	if x == 1:
		return 1
	else:
		return x - subfact(x - 1)
