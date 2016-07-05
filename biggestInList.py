# Write a function that returns the largest element in a list.

list = ['apples', 'mandarins', 'grapes', 'pears', 'bananas']

def biggestOne(list):
    biggest = ''
    for item in list:
        if len(item) > len(biggest):
            biggest = item

    return biggest

print(biggestOne(list))
