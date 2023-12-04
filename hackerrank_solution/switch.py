def f(x):
    return {
        'a':1,
        'b':2
    }.get(x, 9)

print(f(1))
