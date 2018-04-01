#!/usr/bin/env python3


from random import choice


def main():
	words = 'stupid cool clever dumb awesome smelly dave steven person marp creeper'.split()
	user = get_user()
	print(f'\n\n{user} is {choice(words)}!\n\n')
	benny(user)


def get_user():
	return input('\n\nWhat is your name? ')


def benny(user):
	ui = input('Are you a benny tied to a tree? ')
	if ui.lower() in set(['y', 'yes']):
		print('HAHAHAHA YOU\'RE A BENNY TIED TO A TREE!')
	else:
		print('BENNY ON THE LOOSE! ' * 2)


def jaarb():
	raise NotImplementedError()



if __name__ == '__main__':
    main()
