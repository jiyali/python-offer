# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
#
# 示例:
# 输入: S = "a1b2"
# 输出: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# 输入: S = "3z4"
# 输出: ["3z4", "3Z4"]
#
# 输入: S = "12345"
# 输出: ["12345"]


class Solution:
    def letterCasePermutation(self, S):
        if not S:
            return []

        res = []

        def backtack(i, S):
            res.append(S)
            for j in range(i, len(S)):
                if 'a' <= S[j] <= 'z':
                    backtack(j + 1, S[:j] + S[j].upper() + S[j + 1:])
                elif 'A' <= S[j] <= 'Z':
                    backtack(j + 1, S[:j] + S[j].lower() + S[j + 1:])
            return

        backtack(0, S)
        return res


s = Solution()
print(s.letterCasePermutation('a1b2'))
