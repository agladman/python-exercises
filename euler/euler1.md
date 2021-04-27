# Euler 1
## Problem
From: https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.



## Attempts at solution
**1a**. A very basic first attempt. Works OK but probably not all that efficient, plus it doesn't exlucde numbers that are multiples of both 3 and 5.

Gives answer 233168.

**1b**. Slightly better. Steps through loops of 3s and then 5s. Adds increments to the sum and for the second loop exluces those which are also multiples of 3.

Also gives answer 233168. Maybe 1a was already exluding double multiples?

**2**. I think I can do better still by using recursion.
