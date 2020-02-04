# 插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
# 它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。


class Solution():
    def insertSort(self, arr):
        if not arr or len(arr) < 2:
            return arr

        for i in range(1, len(arr)):
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                else:
                    break
        return arr


s = Solution()
print(s.insertSort([12, 11, 13, 5, 6]))
