# 题目：统计一个数字在排序数组中出现的次数。
#       例如，输入排序数组{1,2,3,3,3,3,4,5}和数字3，由于3在这个数组中出现了4次，因此输出4.


# 常规思路：二分法查找大于等于k的第一个数字的下标和大于等于k+1的第一个数字的下标，相减
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if len(data) == 0:
            return 0

        return self.GetFirstK(data, k + 1) - self.GetFirstK(data, k)

    def GetFirstK(self, data, k):
        if data[0] == k:
            return 0

        left = 0
        right = len(data) - 1

        while left < right:
            mid = left + (right - left) // 2
            if data[mid] >= k:
                right = mid
            else:
                left = mid + 1

        if data[left] != k:
            if data[len(data) - 1] < k:
                return len(data)
            elif data[0] > k:
                return 0
        return left


# 思路二：


alist = [1, 2, 3, 3, 3, 3, 4, 5]
s = Solution()
print(s.GetNumberOfK(alist, 3))
