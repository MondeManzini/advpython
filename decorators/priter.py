from __future__ import print_function
'''
def printer(fn):
    def inner(*args, **kwargs):
        print 'entering', fn.__name__
        out = fn(*args, **kwargs)
        print out
        return out
    return inner
'''
def printer_args(prefix=None, pr=print):
    def real_printer(fn):
        def inner(*args, **kwargs):
            pr(prefix + 'entering' + fn.__name__)
            out = fn(*args, **kwargs)
            pr(prefix+str(out))
            return out
        return inner
    return real_printer

@printer_args('****')
def square(x):
    return x**2

#@printer
def cube(x):
    return x**3


square(3)
cube(3)
