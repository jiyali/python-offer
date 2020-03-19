# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return []

        res = []

        def backtrack(string, left, right):
            if len(string) == 2 * n:
                res.append(string)
                return
            if left < n:
                backtrack(string + '(', left + 1, right)
            if right < left:
                backtrack(string + ')', left, right + 1)

        backtrack('', 0, 0)
        return res


s = Solution()
print(s.generateParenthesis(3))
