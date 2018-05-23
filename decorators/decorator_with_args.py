#!/usr/bin/env python3

def make_x(factor):
    def real_make_x(fn):
        def inner(*args,**kwargs):
            return factor*fn(*args,**kwargs)
        return inner
    return real_make_x

@make_x(3)
def square(x):
    return x**2

print square(2)
