#!/usr/bin/env python3

from functools import wraps

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def func(x):
    print(x)

func("Tequila!")
