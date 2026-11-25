# time : O(n)
# space: O(1)
def rotate_array(arr: list[int]) -> None:
    n = len(arr)

    for i in range(n - 2, -1, -1):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # i = n - 2
    # while i > -1:
    #     arr[i], arr[i + 1] = arr[i + 1], arr[i]
    #     i -= 1


arr = list(map(int, input().split()))
print(arr)
rotate_array(arr)
print(arr)
