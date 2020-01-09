# 给定一个含有 n 个正整数的数组和一个正整数 s ，
# 找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
# 思路：双指针


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i = 0
        j = 0
        res = 0
        nums_len = len(nums) + 1

        for j in range(len(nums)):
            res += nums[j]
            while i <= j and res >= s:
                nums_len = min(nums_len, j - i + 1)
                res -= nums[i]
                i += 1
        if nums_len == len(nums) + 1:
            return 0
        else:
            return nums_len


s = Solution()
print(s.minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3]))
