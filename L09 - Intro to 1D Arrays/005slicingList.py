arr = [10, 20, 30, 40, 50]

# print(arr[-1::-1])

print(arr[1:4])
print(type(arr[1:4]))
print(len(arr[1:4]))

print(arr[0:3])
print(type(arr[0:3]))
print(len(arr[0:3]))

print(arr[:3])
print(type(arr[:3]))
print(len(arr[:3]))

print(arr[3:5])
print(type(arr[3:5]))
print(len(arr[3:5]))

print(arr[3:])
print(type(arr[3:]))
print(len(arr[3:]))

brr = arr[2:4]
print(type(brr))
print(brr)
print(len(brr))

brr[0] += 1

print(arr)
print(brr)

crr = arr[:]
print(type(crr))
print(len(crr))
print(crr)

print(arr[1:4:2])

print(arr[::-1])

colors = ["red", "green", "blue", "white"]
colors[1:3] = ["black"]
print(colors)
