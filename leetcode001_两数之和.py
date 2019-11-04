# 题目：


class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return None
        if len(nums) == 2 and sum(nums) == target:
            return 0, 1

        dic = {}
        for i in range(len(nums)):
            if target - nums[i] not in dic:
                dic[nums[i]] = i
            else:
                return dic[target - nums[i]], i