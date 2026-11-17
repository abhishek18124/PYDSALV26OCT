n = int(input())
k = int(input())

mask = ~(1 << k)
print(n & mask)
