n = int(input())

# if n == 0:
#     print(0)
# elif n == 1:
#     print(1)
# else:
#     # n >= 2
#     ...


if n == 0 or n == 1:
    print(n)
else:
    # n >= 2
    a = 0  # 0th fib. no.
    b = 1  # 1st fib. no.

    for _ in range(n - 1):
        c = a + b
        a = b
        b = c

    print(c)  # print(b)

# #iterations = n - 1 ~ n
# time spent in each iteration = const
# time : n.const ~ O(n)

# space: O(1), auxillary space is independent of input size
