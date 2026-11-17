n = int(input())

if n & 1:
    # 0th bit of n is 1 therefore n is odd
    print("odd")
else:
    # 0th bit of n is 0 therefore n is even
    print("even")
