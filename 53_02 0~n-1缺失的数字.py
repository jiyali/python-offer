# 题目：一个长度为 n-1 的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围 0 到 n-1 之内。
#       在范围 0 到 n-1 的 n 个数字中有且只有一个数字不在该数组中，请找出这个数字。


# 常规二分法
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


# 改进二分法
class Solution1(object):
    def getMissingNumber(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] != mid:
                if nums[mid - 1] == mid - 1:
                    return mid
                right = mid - 1
            else:
                left = mid + 1
        return left


s = Solution1()
print(s.getMissingNumber([0]))
print(s.getMissingNumber([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26,
                          27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]))
