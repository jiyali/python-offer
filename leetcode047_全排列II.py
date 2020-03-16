# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


class Solution:
    def permuteUnique(self, nums):
        if not nums:
            return []

        res = []
        nums.sort()

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                else:
                    backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


s = Solution()
print(s.permuteUnique([1, 1, 2]))
