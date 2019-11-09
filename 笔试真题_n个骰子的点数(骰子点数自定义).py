# 题目：有一种特殊的骰子，其点数分别为0、1、2、2、3、3,，现在有n个这种骰子(n最大值为25)，将它们一起扔在地上，
#       所有骰子朝上一面的点数之和为s。求s所有的可能值及其排列组合的数量。
# 输入描述：输入骰子的数量n
# 输出描述：根据s的数值从小到大依次输出其值及其排列组合的数量


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
