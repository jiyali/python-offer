# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]


class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []

        def backtrack(i, tmp_sum, tmp):
            if tmp_sum > target or i == len(candidates):
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            backtrack(i, tmp_sum+candidates[i], tmp+[candidates[i]])
            backtrack(i+1, tmp_sum, tmp)

        backtrack(0, 0, [])
        return res


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
