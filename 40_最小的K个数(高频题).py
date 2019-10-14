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


class Solution1(object):
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput is None or len(tinput) < k or k <= 0 or len(tinput) <= 0:
            return []

        length = len(tinput)

        left = 0
        right = length - 1

        index = self.Partition(tinput, left, right)

        while index != k - 1:
            if index > k - 1:
                right = index - 1
                index = self.Partition(tinput, left, right)
            else:
                left = index + 1
                index = self.Partition(tinput, left, right)
        output = tinput[:k]
        output.sort()
        return output

    def Partition(self, numbers, left, right):

        pivot = numbers[left]

        while left < right:
            while left < right and numbers[right] >= pivot:
                right -= 1
            numbers[left], numbers[right] = numbers[right], numbers[left]
            while left < right and numbers[left] <= pivot:
                left += 1
            numbers[left], numbers[right] = numbers[right], numbers[left]

        return left


# 思路三：在不能改变数组的情况下，且数据量巨大，时间复杂度O(nlogk)
import heapq


class Solution2(object):
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput is None or len(tinput) < k or len(tinput) <= 0 or k <= 0:
            return []

        output = []

        for number in tinput:
            if len(output) < k:
                output.append(number)
            else:  # 构建最大堆
                output = heapq.nlargest(k, output)
                if number >= output[0]:
                    continue
                else:
                    output[0] = number
        return output[::-1]


# 思路四：sorted排序，输出前k个即可，时间复杂度为O(nlogn)
class Solution3(object):
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or len(tinput) < k:
            return []
        tinput = sorted(tinput)
        return tinput[:k]


tinput = [4, 5, 1, 6, 2, 7, 3, 8]
s = Solution2()
print(s.GetLeastNumbers_Solution(tinput, 4))
print(s.GetLeastNumbers_Solution(tinput, 5))
