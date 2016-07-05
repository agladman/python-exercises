# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

print('Enter a number: ')
num = int(input())
sum = 0

for i in range(0, num):
    sum = sum + i

sum = sum + num

print(sum)
