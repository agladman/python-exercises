# Write a function that returns the largest element in a list.

mylist = ['apples', 'mandarins', 'grapes', 'pears', 'bananas']

def find_biggest(mylist):
    biggest = ''
    for item in mylist:
        if len(item) > len(biggest):
            biggest = item
    return biggest

print(find_biggest(mylist))
