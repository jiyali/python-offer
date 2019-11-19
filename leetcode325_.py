# 题目：给定一个数组 nums 和一个目标值 k，找到和等于 k 的最长子数组长度。
#       如果不存在任意一个符合要求的子数组，则返回 0。
# 注意: nums 数组的总和是一定在 32 位有符号整数范围之内的


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = {}
        cur_sum, max_len = 0, 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum == k:
                max_len = i + 1
            elif cur_sum - k in sums:
                max_len = max(max_len, i - sums[cur_sum - k])
            if cur_sum not in sums:
                sums[cur_sum] = i  # Only keep the smallest index.
        return max_len

    def max_length(self, nums, k):  # 大于k的最长子数组
        sums = {}
        cur_sum, max_len = 0, 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum > k:
                max_len = i + 1
            elif cur_sum - k in sums:
                max_len = max(max_len, i - sums[cur_sum - k])
            if cur_sum not in sums:
                sums[cur_sum] = i  # Only keep the smallest index.
        return max_len


s = Solution()
print(s.max_length(nums=[1, -1, 5, -2, 3], k=3))
print(s.max_length(nums=[-1, 1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1], k=0))
print(s.max_length(nums=[1, 1, -1, -1], k=0))
