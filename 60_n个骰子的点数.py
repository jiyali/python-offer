# 题目：把n个骰子仍在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。


class Solution(object):
    def get_ans(self, n):
        dp = [[0 for i in range(6 * n)] for i in range(n)]
        # print(dp)

        for i in range(6):
            dp[0][i] = 1
        # print(dp)

        for i in range(1, n):  # 从第2个骰子开始
            for j in range(i, 6 * (i + 1)):  # [0,i-1]的时候，频数为0（例如2个骰子不可能投出点数和为1）
                dp[i][j] = dp[i - 1][j - 6] + dp[i - 1][j - 5] + dp[i - 1][j - 4] + \
                           dp[i - 1][j - 3] + dp[i - 1][j - 2] + dp[i - 1][j - 1]

        count = dp[n - 1]
        # return count  # 算得骰子投出每一个点数的频数。再除以总的排列数即可得到频率
        # print(count)
        # other = []
        all = float(6**n)
        # 第i个元素代表骰子总和为n+i
        for i, item in enumerate(count):
            pro = float(item / all)
        #     other.append([i+1, pro])
        # return other
            print("{}: {:e}".format(i+1, pro))


s = Solution()
print(s.get_ans(5))
