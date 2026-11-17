n = int(input())
k = int(input())

if (n >> k) & 1:
    # bit 0 of n' is set i.e. kth bit of n is set
    print(True)
else:
    # bit 0 of n' is not set i.e. kth bit of n is not set
    print(False)
