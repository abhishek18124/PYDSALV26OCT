# time : in worst case O(n^2) e.g. [50, 40, 30, 20, 10]
# time : in best case : O(n) e.g. [10, 20, 30, 40, 50]
def bubble_sort(arr: list[int], n: int) -> None:
    cmp = 0

    for i in range(1, n):  # [1, n) i.e. [1, n-1]
        # in the ith pass, place the largest element
        # in the unsorted part of the array to its
        # correct position

        flag = False  # assume no swaps will be done in the ith pass

        for j in range(0, n - i):  # [0, n-i) i.e. [0, n-i-1]
            cmp += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True

        if flag == False:
            # no swaps were done in the ith pass which means array is already sorted and we don't need to run any more passes
            break

    print(cmp)


arr = list(map(int, input().split()))
n = len(arr)

print(arr)  # 10 20 30 40 50

bubble_sort(arr, n)

print(arr)  # 10 20 30 40 50
