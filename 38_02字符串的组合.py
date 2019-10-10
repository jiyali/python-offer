# 题目：输入一个字符串,按字典序打印出该字符串中字符的所有组合。
#       例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串a、b、c、ab、ac、bc、abc。


import itertools


class Solution(object):
    def Combination(self, ss):
        if not ss:
            return []

        output = []

        for i in range(1, len(ss)+1):
            list1 = list(map(''.join, itertools.combinations(sorted(ss), i)))
            output.append(list1)

        return output


ss = 'acb'
S = Solution()
print(S.Combination(ss))