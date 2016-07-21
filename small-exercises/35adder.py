# Modify the previous program such that only multiples of three or five
# are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

print('Enter a number: ')
num = int(input())
sum = 0

for i in range(0, num):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i

sum = sum + num

print(sum)
