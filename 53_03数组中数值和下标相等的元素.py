# 题目：假设一个单调递增的数组里的每个元素都是整数并且是唯一的。
#       请编程实现一个函数找出数组中任意一个数值等于其下标的元素。
#       例如，在数组 [−3,−1,1,3,5] 中，数字 3 和它的下标相等。


class Solution(object):
    def getNumberSameAsIndex(self, nums):
        if len(nums) == 0:
            return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left + 1) // 2
            if nums[mid] == mid:
                return mid
            if nums[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        return -1


s = Solution()
print(s.getNumberSameAsIndex([0]))
print(s.getNumberSameAsIndex([-3, -1, 1, 3, 5]))
print(s.getNumberSameAsIndex([0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]))

