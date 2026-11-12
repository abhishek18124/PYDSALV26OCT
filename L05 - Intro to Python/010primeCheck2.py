n = int(input())

for i in range(2, n):  # [2, n) i.e. [2, n-1]
    if n % i == 0:
        # we've found a factor of n in the range [2, n-1]
        print(n, " is not prime")
        break
else:
    # this block runs only when you exit the loop without break
    print(n, " is a prime")
