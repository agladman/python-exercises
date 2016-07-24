#!/usr/bin/env Python3

end = 1000
sum = 0
# we can step through loops
for i in range(3, end, 3):
    sum += i

for i in range(5, end, 5):
    if i % 3 != 0:
        sum += i

print(sum)
