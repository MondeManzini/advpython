from functools import wraps
def debug(method):
    @wraps(method)
    def inner(*args, **kwargs):
        print 'entering', method.__name__
        out = method(*args,**kwargs)
        print 'returns',out
        return out
    return inner

def debugclass(cls):
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls


