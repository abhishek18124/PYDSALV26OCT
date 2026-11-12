n = int(input())
s = 0  # to track the sum of digits

while n != 0:
    d = n % 10
    s = s + d
    n = n // 10

print(s)
