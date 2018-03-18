#!/usr/bin/env python3


import time

def timing_func(some_func):

	"""
	Outputs the time taken to execute a function
	"""

	def wrapper():
		t1 = time.time()
		some_func()
		t2 = time.time()
		return f'Time it took to run the function: {str((t2 - t1))}\n'

	return wrapper

@timing_func
def muh_func():
	numz = []
	for num in (range(0, 10000)):
		numz.append(num)
	print(f'\nSum of all the numbers: {str(sum(numz))}.')


print(muh_func())
