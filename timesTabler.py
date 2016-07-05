# Write a program that prints a multiplication table for numbers up to 12.

for i in range(1, 13):
    for j in range(1, 13):
        print('%i x %i is %i\n' % (i, j, i * j))
    print('\n')
