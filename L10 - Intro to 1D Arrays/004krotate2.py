class Solution:
    def rotate(self, arr: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)

        for _ in range(k):
            for i in range(n - 2, -1, -1):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
