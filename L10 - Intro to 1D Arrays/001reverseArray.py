import copy


# time : O(n)
# space: O(1)
def reverse_array(arr: list[int]) -> None:
    i = 0
    j = len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


arr = list(map(int, input().split()))

print(arr)

# print(type(arr))
# print(len(arr))
# print(arr)

reverse_array(arr)

print(arr)

brr = [1, 2, 3, 4, 5]
print(brr)
# rev_cpy_brr = brr[::-1]
x = brr.reverse()
print(x)
print(brr)
# print(rev_cpy_brr)

crr = [10, 20, 30, 40, 50]
drr = copy.deepcopy(crr)  # crr
