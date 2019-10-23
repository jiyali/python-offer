# 题目：一个长度为 n-1 的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围 0 到 n-1 之内。
#       在范围 0 到 n-1 的 n 个数字中有且只有一个数字不在该数组中，请找出这个数字。


class Solution(object):
    def getMissingNumber(self, nums):
        if nums is None or len(nums) == 0:
            return 0

        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > mid:
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
print(s.getMissingNumber([0]))
