#!/usr/bin/env python3

from functools import wraps,partial
def make_x(factor, fn=None):
    if not fn: 
        return partial(make_x,factor)
    @wraps(fn)
    def inner(*args,**kwargs):
        return factor*fn(*args,**kwargs)
    return inner

@make_x(3)
def square(x):
    return x**2

print square(2)
