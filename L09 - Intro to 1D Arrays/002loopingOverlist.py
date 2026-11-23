arr = [10, 20, 30, 40, 50]
n = len(arr)

# i = 0
# while i < n:
#     print(arr[i])
#     i += 1

# for num in arr:
#     print(num, end=" ")

# for i in range(n):
#     print(i, arr[i])

# for i, num in enumerate(arr):
#     print(i, num)

for item in enumerate(arr):
    print(type(item))
    print(item)
