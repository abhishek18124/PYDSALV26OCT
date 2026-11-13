n = int(input())

i = 1
num = 1

while i <= n:
    # for the ith row, print i numbers

    j = 1

    while j <= i:
        print(num, end=" ")
        num = num + 1
        j = j + 1

    i = i + 1

    print()

num = 1

for i in range(1, n + 1):
    # for the ith row, print i numbers
    for _ in range(i):
        print(num, end=" ")
        num = num + 1
    print()
