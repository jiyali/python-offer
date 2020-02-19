# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# dp方程：总和为 n 的最小完全平方数个数 = min(总和为 (n - 某个完全平方数) 的最小完全平方数个数) + 1
# 时间复杂度：O(N^2) 空间复杂度：O(N)


class Solution:
    def numSquares(self, n):
        # 动态规划
        dp = [i for i in range(n + 1)]
        m = 1
        while m * m <= n:
            for i in range(m * m, n + 1):
                dp[i] = min(dp[i], dp[i - m * m] + 1)
            m += 1
        return dp[-1]

    def numSquares_bfs(self, n):
        # bfs 所有可能的平方数是从1到floor(sqrt(n))，找到最小的层数刚好满足和为n
        # Time O(n**n/2) SpaceO(n)
        queue = [(n, 0)]
        while queue:
            res, depth = queue.pop(0)
            k = int(res ** 0.5)
            for i in range(k, 0, -1):
                new_res = res - i ** 2
                if new_res == 0:
                    return depth + 1
                queue.append((new_res, depth + 1))
        return res


s = Solution()
print(s.numSquares(12))
print(s.numSquares_bfs(12))
