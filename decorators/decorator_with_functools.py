#!/usr/bin/env python3
from functools import wraps

def make_double(fn):
    @wraps(fn)
    def inner(*args,**kwargs):
        return 2*fn(*args,**kwargs)
    return inner

@make_double
def square(x):
    'returns the square of x'
    return x**2

#square = make_double(square)

