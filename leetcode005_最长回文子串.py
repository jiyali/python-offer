# 题目： 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。


class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2 or s == s[::-1]:
            return s

        start, maxlength = 0, 1
        for i in range(len(s)):
            odd = s[i - maxlength - 1:i + 1]  # 奇数
            even = s[i - maxlength:i + 1]  # 偶数
            if i - maxlength - 1 >= 0 and odd == odd[::-1]:
                start = i - maxlength - 1
                maxlength += 2
            elif i - maxlength >= 0 and even == even[::-1]:
                start = i - maxlength
                maxlength += 1
        return s[start:start + maxlength]

    def longestPalindrome1(self, s):
        # 动态规划
        if not s:
            return ""
        res = ""
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = 0
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                if dp[j][i] and max_len < i + 1 - j:
                    res = s[j: i + 1]
                    max_len = i + 1 - j
        return res


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome1("babad"))
