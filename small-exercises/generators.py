#!/usr/bin/env python3


"""Playing with generators to figure out how they work once and for all."""


def spellout(text):
	for ch in text:
		yield ch


def addone(my_int):
	"""Not veru useful as a generator, no iteration required so better as a normal function returning a value."""
	yield my_int + 1


def countup(my_int):
	for _ in range(my_int):
		yield _ + 1


def countdown(my_int):
	for _ in range(my_int, 0, -1):
		yield _


def main():
	print('\nspell out "bumhole"')
	string = ', '.join(c for c in spellout('bumhole'))
	print(string)
	print('\ncount up to 5')
	for _ in countup(5):
		print(_)
	print('\ncount down from 5')
	for _ in countdown(5):
		print(_)


if __name__ == '__main__':
    main()

