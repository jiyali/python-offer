# 题目：把n个骰子仍在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。


class Solution(object):
    def get_ans(self, n):
        dp =[[0 for i in range(6*n+1)] for j in range(n+1)]
        # print(dp)

        for i in range(1, 7):  # 如果只有一个骰子：dp(1, 1) =dp(1, 2) =dp(1, 3) =dp(1, 4) =dp(1, 5) =dp(1, 6) =1
            dp[1][i] = 1
        # print(dp)

        for i in range(2, n + 1):  # 从第2个骰子开始
            for j in range(i, 6 * i + 1):  # [0, i-1]的时候，频数为0
                # 在c-1个骰子的基础上，再增加一个骰子出现点数和为k的结果只有这6种情况，所以
                # dp(c, k) =dp(c-1, k-1) +dp(c-1, k-2) +dp(c-1, k-3) +dp(c-1, k-4) +dp(c-1, k-5) +dp(c-1, k-6)
                dp[i][j] = dp[i - 1][j - 6] + dp[i - 1][j - 5] + dp[i - 1][j - 4] + \
                           dp[i - 1][j - 3] + dp[i - 1][j - 2] + dp[i - 1][j - 1]

        count = dp[n]
        # print(count)

        # other = []
        total = float(6**n)
        # 第i个元素代表骰子总和为n+i
        for i, item in enumerate(count):
            pro = float(item / total)
        #     other.append([i+1, pro])
        # return other
            print("{}: {:e}".format(i, pro))


s = Solution()
print(s.get_ans(4))

