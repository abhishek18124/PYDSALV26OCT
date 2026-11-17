n = int(input())
cnt = 0

# time : ~ logn.const ~ O(logn)
# space: O(1)

while n != 0:
    if n & 1:
        # 0th of n is set
        cnt += 1

    n = n >> 1

print(cnt)
