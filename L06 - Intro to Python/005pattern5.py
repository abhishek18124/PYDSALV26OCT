n = int(input())

i = 1

while i <= n:
    # for the ith row print n-i spaces

    j = 1

    while j <= n - i:
        print(" ", end="")
        j = j + 1

    # followed by i stars

    j = 1

    while j <= i:
        print("*", end="")
        j = j + 1

    i = i + 1

    print()

for i in range(1, n + 1):
    # for the ith row print n-i spaces
    for _ in range(n - i):
        print(" ", end="")

    # followed by i stars
    for _ in range(i):
        print("*", end="")

    print()

for i in range(1, n + 1):
    # for the ith row print n-i spaces
    print(" " * (n - i), end="")

    # followed by i stars
    print("*" * i)
