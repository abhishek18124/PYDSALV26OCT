n = int(input())

print(n.bit_count())

cnt = 0

# time : # no. of set bits in n
# space: O(1)

while n != 0:
    cnt += 1
    n = n & (n - 1)  # turns off rightmost set bit of n

print(cnt)
