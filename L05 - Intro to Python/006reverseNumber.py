n = int(input())

ans = 0

while n != 0:
    d = n % 10
    ans = ans * 10 + d
    n = n // 10

print(ans)
