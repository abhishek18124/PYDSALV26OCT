n = int(input())
m = n - n // 2

# print the upper part of the pattern

for i in range(1, m + 1):
    # for the ith row print m-i spaces
    for _ in range(m - i):
        print(" ", end="")

    # followed by 2i - 1 stars
    for _ in range(2 * i - 1):
        print("*", end="")

    print()

# print the lower part of the pattern

for i in range(1, m):
    # for the ith row, print i spaces
    for _ in range(i):
        print(" ", end="")

    # followed by n-2i stars
    for _ in range(2 * (m - i) - 1):  # n - 2 * i
        print("*", end="")

    print()
