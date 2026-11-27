def insertion_sort(arr: list[int], n: int) -> None:
    for i in range(1, n):  # [1, n) i.e. [1, n-1]
        key = arr[i]
        # in the ith pass, our task is to insert the
        # key to its correct position in the sorted
        # part of the array i.e. arr[0...i-1]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


arr = list(map(int, input().split()))
n = len(arr)

print(arr)  # 10 20 30 40 50

insertion_sort(arr, n)

print(arr)  # 10 20 30 40 50
