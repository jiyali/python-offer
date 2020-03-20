# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]


class Solution:
    def combinationSum3(self, k, n):
        res = []

        def backtrack(nums, tmp_sum, tmp):
            if tmp_sum == n and len(tmp) == k:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[i + 1:], tmp_sum + nums[i], tmp + [nums[i]])

        nums = [i for i in range(1, 10)]
        backtrack(nums, 0, [])
        return res


s = Solution()
print(s.combinationSum3(k=3, n=7))
