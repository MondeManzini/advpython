def multi(fn):
    fns = []
    for i in range(3):
        def inner(*args, **kwargs):
            return fn(*args, **kwargs) * i
        fns.append(inner)
    return fns

def square(x):
    return x**2

square_1, square_2, square_3 = multi(square)

# What do you expect this to print?
print square_1(2), square_2(2), square_3(2)
