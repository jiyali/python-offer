# 题目：给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
#       你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。


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