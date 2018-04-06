#!/usr/bin/env python3


"""Prints items from a dict into formatted tables.
	USAGE: printPicnic(itemsDict, leftWidth, rightWidth)
	leftWidth is the width for the item labels column, rightWidth is for the values column
	 """


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS' .center(leftWidth + rightWidth, '-'))
    for k, v, in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
