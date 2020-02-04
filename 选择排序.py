# 选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。
# 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
# 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
# 以此类推，直到所有元素均排序完毕
# 时间复杂度O(n^2),空间复杂度O(1)


class Solution():
    def SelectionSort(self, arr):
        if not arr or len(arr) < 2:
            return arr

        for i in range(len(arr)):
            min = i
            for j in range(i + 1, len(arr)):
                if arr[min] > arr[j]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
        return arr


s = Solution()
print(s.SelectionSort([-9, -8, 640, 25, 12, 22, 33, 23, 45, 11, -2, -5, 99, 0]))
