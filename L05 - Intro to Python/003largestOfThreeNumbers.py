a, b, c = map(int, input().split())

if a > b and a > c:
    print(a)
else:
    # either b or c
    if b > c:
        print(b)
    else:
        print(c)

if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)
