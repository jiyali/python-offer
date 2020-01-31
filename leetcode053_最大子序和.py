# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。


class Solution:
    def maxSubArray(self, nums):
        # 普通做法
        cur_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(cur_sum, max_sum)
        return max_sum

    def maxSubArray1(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
