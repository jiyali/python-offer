# 题目：输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。


# 思路一：快速排序之后 输出前k个数字即可
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


tinput = [4, 5, 1, 6, 2, 7, 3, 8]
s = Solution()
print(s.GetLeastNumbers_Solution(tinput, 4))
print(s.GetLeastNumbers_Solution(tinput, 5))
