n = int(input())

i = 1

while i <= n:
    if i % 2 == 1:
        num = 1
    else:
        num = 0

    j = 1

    while j <= i:
        print(num, end=" ")
        # num = 1 - num
        # num = not num
        if num == 0:
            num = 1
        else:
            num = 0
        j = j + 1

    i = i + 1
    print()

for i in range(1, n + 1):
    # if i % 2 == 1:
    #     num = 1
    # else:
    #     num = 0

    num = 1 if i % 2 == 1 else 0

    for _ in range(i):
        print(num, end=" ")
        num = 1 - num

    print()
