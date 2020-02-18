# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# dp方程：总和为 n 的最小完全平方数个数 = min(总和为 (n - 某个完全平方数) 的最小完全平方数个数) + 1
# 时间复杂度：O(N^2) 空间复杂度：O(N)


class Solution:
    def numSquares(self, n):
        dp = [i for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, int(i ** (0.5)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[-1]


s = Solution()
print(s.numSquares(12))
