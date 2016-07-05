"""Write a program that prints all prime numbers. (Note: if your programming
language does not support arbitrary size numbers, printing all primes up to
the largest number you can easily represent is fine too.)"""

# first attempt limiting this to 10

primes = []

for i in range(2, 10):
    for j in range(2, i):
        if i % j != 0:
            primes.append(i)

print(primes)

# not working and I don't know why
