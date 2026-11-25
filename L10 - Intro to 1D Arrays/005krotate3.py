class Solution:
    # time : O(n)
    # space: O(1)
    def rotate(self, arr: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse_array(i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        n = len(arr)
        k = k % n

        # 1. reverse the entire array i.e. arr[0...n-1]
        arr.reverse()  # reverse_array(0, n-1)

        # 2. reverse the 1st k terms i.e. arr[0...k-1]
        reverse_array(0, k - 1)

        # 3. reverse the last n-k terms i.e. arr[k...n-1]
        reverse_array(k, n - 1)
