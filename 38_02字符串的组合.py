# 题目：输入一个字符串,按字典序打印出该字符串中字符的所有组合。
#       例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串a、b、c、ab、ac、bc、abc。


# 第一种方法：暂时输出为['a', 'ab', 'ac', 'acb', 'b', 'c', 'cb']，能力有限，后期来改进
class Solution(object):
    def Combination(self, ss):
        if len(ss) == 0:
            return []
        if len(ss) == 1:
            return [ss]

        output = set()

        for i in range(len(ss)):
            output.add(ss[i])
            for j in self.Combination(ss[i+1:]):
                output.add(ss[i] + j)

        return sorted(output)


# 另一种方法：itertools.combinations用于生成一个组合

import itertools
from functools import reduce


class Solution1(object):
    def Combination(self, ss):
        if not ss:
            return []

        output = []

        for i in range(1, len(ss)+1):
            list1 = list(map(''.join, itertools.combinations(sorted(ss), i)))
            output.append(list1)

        return reduce(lambda x, y: x + y, output)


ss = 'acb'
S = Solution()
S1 = Solution1()
print(S.Combination(ss))
print(S1.Combination(ss))
