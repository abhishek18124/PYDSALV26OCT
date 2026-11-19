def add(a, b, c=0) -> int:
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    return a + b + c


print(add(2, 3, 5))
print(add(b=3, c=5, a=2))
print(add(2, 3))
