# 归并排序（英语：Merge sort，或mergesort），是创建在归并操作上的一种有效的排序算法。
# 该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
#
# 分治法:
# 分割：递归地把当前序列平均分割成两半。
# 集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。


class Solution:
    def MergeSort(self, arr):
        if len(arr) < 2:
            return arr

        mid = len(arr) // 2

        left = self.MergeSort(arr[:mid])
        right = self.MergeSort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        i = j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:]
        res += right[j:]
        return res


s = Solution()
print(s.MergeSort([3, 5, 7, 1, 4, 2]))
