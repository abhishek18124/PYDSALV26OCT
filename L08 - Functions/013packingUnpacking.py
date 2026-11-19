def f():
    return 2, 3, 5


x = f()
a, b, c = x
print(type(x))
print(x)
print(type(a), type(b), type(c))
print(a, b, c)


def g(a, b, *args):
    print(a, type(a))
    print(b, type(b))
    print(type(args))
    print(args)


g(1, 2, 3, 4, 5)


def h(**kwargs):
    print(type(kwargs))
    print(kwargs)


h(a=2, b=3, c=4, f=5, d=6)
