# 将一个大的无序数组有序，我们可以把大的数组分成两个，然后对这两个数组分别进行排序，之后在把这两个数组合并成一个有序的数组。
# 由于两个小的数组都是有序的，所以在合并的时候是很快的。#
# 通过递归的方式将大的数组一直分割，直到数组的大小为 1，此时只有一个元素，那么该数组就是有序的了，
# 之后再把两个数组大小为1的合并成一个大小为2的，再把两个大小为2的合并成4的 ….. 直到全部小的数组合并起来。
# 性质：1、时间复杂度：O(nlogn)  2、空间复杂度：O(n)  3、稳定排序  4、非原地排序


class Solution:
    def MergeSort(self, arr):
        if len(arr) < 2:
            return arr

        mid = len(arr) // 2

        left = self.MergeSort(arr[:mid])  # T(n/2)
        right = self.MergeSort(arr[mid:])  # T(n/2)

        return self.merge(left, right)  # O(n)
    # T(N) = 2T(N/2) + O(N)

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


class Solution1:
    def merge(self, arr, low, mid, high):
        left = arr[low: mid]
        right = arr[mid: high]
        k = 0
        j = 0
        result = []
        while k < len(left) and j < len(right):
            if left[k] <= right[j]:
                result.append(left[k])
                k += 1
            else:
                result.append(right[j])
                j += 1
        result += left[k:]
        result += right[j:]
        arr[low: high] = result

    def MergeSort(self, arr):
        i = 1  # i是步长
        while i < len(arr):
            low = 0
            while low < len(arr):
                mid = low + i  # mid前后均为有序
                high = min(low + 2 * i, len(arr))
                if mid < high:
                    self.merge(arr, low, mid, high)
                low += 2 * i
            i *= 2
        return arr


s1 = Solution()
s2 = Solution1()
print(s1.MergeSort([3, 5, 7, 1, 4, 2]))
print(s2.MergeSort([3, 5, 7, 1, 4, 2]))
