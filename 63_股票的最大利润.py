# 题目：假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可获得的最大利润是多少？
#       例如一只股票在某些时间节点的价格为 [9, 11, 8, 5, 7, 12, 16, 14]。
#       如果我们能在价格为5的时候买入并在价格为16时卖出，则能收获最大的利润11


class Solution(object):
    def maxDiff(self, nums):
        if not nums or len(nums) == 1:
            return 0

        min_val = nums[0]
        max_diff = nums[1] - min_val

        for i in range(1, len(nums)):
            min_val = min(min_val, nums[i])
            max_diff = max(max_diff, nums[i] - min_val)
        return max_diff


s = Solution()
print(s.maxDiff([9, 11, 8, 5, 7, 12, 16, 14]))
