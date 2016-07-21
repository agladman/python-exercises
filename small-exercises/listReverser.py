# Write function that reverses a list, preferably in place.
# Write a function that returns the elements on odd positions in a list.

list = ['a', 'b', 'c', 'd', 'e']

def swappit(list):
    list.sort(reverse=True)

def odder(list):
    returnlist = []
    for i in range(0, len(list)):
        if i % 2 != 0:
            returnlist += list[i]
    return returnlist

print(list)
swappit(list)
print(list)

print(odder(list))
