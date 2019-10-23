# 题目：统计一个数字在排序数组中出现的次数。
#       例如，输入排序数组{1,2,3,3,3,3,4,5}和数字3，由于3在这个数组中出现了4次，因此输出4.


class Solution(object):
    def GetNumberOfK(self, data, k):
        if len(data) == 0:
            return 0
        if len(data) == 1 and data[0] == k:
            return 1

    def GetFistK(self, data, k):
        