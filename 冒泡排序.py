class Solution:
    def bubbleSort(self, arr):
        if arr is None or len(arr) < 2:
            return arr

        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


s = Solution()
print(s.bubbleSort([64, 34, 25, 12, 22, 11, 90]))
