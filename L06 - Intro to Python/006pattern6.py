n = int(input())

for i in range(1, n + 1):
    # for the ith row print n-i spaces
    for _ in range(n - i):
        print(" ", end="")

    # followed by i nos. starting from i in inc order
    num = i
    for _ in range(i):
        print(num, end="")
        num = num + 1

    print()
