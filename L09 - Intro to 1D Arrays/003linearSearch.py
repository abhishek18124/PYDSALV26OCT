arr = [10, 20, 30, 40, 50]

print(60 in arr)
print(30 in arr)
print(40 in arr)

target = 60

for item in arr:
    if item == target:
        print(True)
        break
else:
    print(False)


flag = False  # assume target is not present in the array

for item in arr:
    if item == target:
        flag = True
        break

print(flag)
