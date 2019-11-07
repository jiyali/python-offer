#
class Solution(object):
    def get_ans(self, n):
        dp =[[0 for i in range(3 * n + 1)] for j in range(n + 1)]
        print(dp)

        for i in range(0, 1):
            # 如果只有一个骰子
            dp[1][0] = 1
            dp[1][1] = 1
            dp[1][2] = 2
            dp[1][3] = 2
        print(dp)

        for i in range(2, n + 1):
            for j in range(0, 3 * i + 1):

                dp[i][j] = dp[i - 1][j - 0] + dp[i - 1][j - 1] + dp[i - 1][j - 2] + \
                           dp[i - 1][j - 2] + dp[i - 1][j - 3] + dp[i - 1][j - 3]

        count = dp[n]
        print(dp)

        # 第i个元素代表骰子总和为n+i
        for i, item in enumerate(count):
            print("{}: {}".format(i, item))


s = Solution()
print(s.get_ans(2))
