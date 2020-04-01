class Solution:
    def shellSort(self, arr):
        if len(arr) < 2:
            return arr
        gap = int(len(arr) / 2)

        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i
                while j >= gap and arr[i - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap = int(gap / 2)
        return arr


s = Solution()
print(s.shellSort([3, 5, 7, 1, 4, 2]))
