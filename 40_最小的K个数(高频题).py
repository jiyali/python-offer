# 题目：输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。


# 思路一：快速排序之后 输出前k个数字即可。时间复杂度O(nlogn)
from random import *


class Solution(object):
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput is None or len(tinput) < k or len(tinput) <= 0 or k <= 0:
            return []

        def quicksort(array):
            if not array:
                return []
            if len(array) < 2:
                return array

            pivot = choice(array)
            less = [i for i in array if i < pivot]
            greater = [i for i in array if i > pivot]

            return quicksort(less) + [pivot] * array.count(pivot) + quicksort(greater)

        tinput = quicksort(tinput)

        return tinput[:k]


# 思路二：寻找更快的方法O(n)：基于Partition思想(仅适用于可以修改数组的情况下)


class Solution2(object):
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput is None or len(tinput) < k or k <= 0 or len(tinput) <= 0:
            return []

        length = len(tinput)

        start = 0
        end = length - 1

        index = self.Partition(tinput, length, start, end)

        while index != k - 1:
            if index > k - 1:
                end = index - 1
                index = self.Partition(tinput, length, start, end)

    def Partition(self, tinput, length, start, end):
        if tinput is None or length < 0 or start < 0 or end > length:
            return None

        if end == start:
            return end

        pivot = tinput[start]

        left = start
        right = end

        while left <right:
            while right



tinput = [4, 5, 1, 6, 2, 7, 3, 8]
s = Solution()
print(s.GetLeastNumbers_Solution(tinput, 4))
print(s.GetLeastNumbers_Solution(tinput, 5))
