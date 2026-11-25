# time : O(kn)
# space: O(1)
def k_rotate_array(arr: list[int], k: int) -> None:
    n = len(arr)

    for _ in range(k):
        for i in range(n - 2, -1, -1):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]


arr = list(map(int, input().split()))
k = int(input())
print(arr)
k_rotate_array(arr, k)
print(arr)
