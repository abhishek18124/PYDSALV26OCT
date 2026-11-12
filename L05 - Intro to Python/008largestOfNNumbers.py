n = int(input())
max_so_far = float("-inf")
min_so_far = float("inf")
for _ in range(n):
    num = int(input())

    if num > max_so_far:
        max_so_far = num

    if num < min_so_far:
        min_so_far = num

print(max_so_far)
print(min_so_far)
