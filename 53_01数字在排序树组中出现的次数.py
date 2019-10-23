# 题目：统计一个数字在排序数组中出现的次数。
#       例如，输入排序数组{1,2,3,3,3,3,4,5}和数字3，由于3在这个数组中出现了4次，因此输出4.


# 常规思路：二分法查找大于等于k的第一个数字的下标和大于等于k+1的第一个数字的下标，相减。时间复杂度O(n)
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


# 思路二：改进二分法，找到数组第mid个数，如果mid小于k，则查找右半段
#                                      如果mid大于k，则查找左半段
#                                      如果mid等于k，则查看前一个数字是否等于k，如果mid-1不等于k，则mid是第一个目标数字
#                                                                             如果mid-1等于k,则目标值在前半段，继续查找
#        根据这种思路我们可以查找到第一个目标值所在的位置，同理也能查找到最后一个目标值所在位置，用最后一个位置-最初一个位置+1即可
# (※推荐)时间复杂度为O(nlogn)
class Solution1(object):
    def GetNumberOfK(self, data, k):
        number = 0
        if data is not None and len(data) > 0:
            first = self.GetFirstK(data, k, 0, len(data) - 1)
            last = self.GetLastK(data, k, 0, len(data) - 1)
            if first > -1:
                number = last - first + 1
        return number

    def GetFirstK(self, data, k, left, right):

        if left > right:
            return -1

        mid = left + (right + 1 - left) // 2

        if data[mid] == k:
            if mid > 0 and data[mid - 1] == k:
                right = mid - 1
            else:
                return mid
        elif data[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

        return self.GetFirstK(data, k, left, right)

    def GetLastK(self, data, k, left, right):

        if left > right:
            return -1

        mid = left + (right - left) // 2

        if data[mid] == k:
            if mid < right and data[mid + 1] == k:
                left = mid + 1
            else:
                return mid
        elif data[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

        return self.GetLastK(data, k, left, right)


alist = [1, 2, 3, 3, 3, 3]
s = Solution1()
print(s.GetNumberOfK(alist, 3))
