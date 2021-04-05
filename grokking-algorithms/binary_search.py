#!/usr/bin/env python3

def binary_search(list, item):
	"iterative version of binary search"
	low = 0
	high = len(list) - 1

	while low <= high:
		mid = (low + high) // 2
		guess = list[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

def binsearch(list, item):
	"recursive version of binary search"
	if len(list) == 1:
		return list[0] if list[0] == item else None
	else:
		mid = (len(list) -1) // 2
		list = list[mid:] if mid < item else list[:mid]
		return binsearch(list, item)



# Base Case: one item (target) in array.
# Recursive Case: cut array by half each recursive call.


def recursive_binary_search(arr, target):
    mid = len(arr) // 2
    if len(arr) == 1:
        return mid if arr[mid] == target else None
    elif arr[mid] == target:
        return mid
    else:
        if arr[mid] < target:
            callback_response = recursive_binary_search((arr[mid:]), target)
            return mid + callback_response if callback_response is not None else None
        else:
            return recursive_binary_search((arr[:mid]), target)
