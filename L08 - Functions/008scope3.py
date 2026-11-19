x = 10


def f():
    x = 20  # right now, local x is shadowing global x
    print(x)


f()
print(x)
