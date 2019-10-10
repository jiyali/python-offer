# 题目：输入一个字符串,按字典序打印出该字符串中字符的所有排列。
#       例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba

# 思路：遍历出所有可能出现在第一个位置的字符,固定第一个字符，递归取得后面的每一个字符的组合
#       这里可以使用集合，集合可以保证没有重复的排列


class Solution(object):
    def Permutation(self, ss):
        if len(ss) == 0:
            return []

        if len(ss) == 1:
            return [ss]

        output = set()

        # 遍历字符串，固定第一个元素
        for i in range(len(ss)):
            # 依次固定后面元素
            for j in self.Permutation(ss[:i] + ss[i+1:]):
                output.add(ss[i] + j)
        return sorted(output)  # sorted() 函数对所有可迭代的对象进行排序操作。


# 另一种方法: itertools.permutations用于生成一个排列


import itertools


class Solution1(object):
    def Permutation(self, ss):
        if not ss:
            return []
        return sorted(list(set(map(''.join, itertools.permutations(ss)))))


ss = 'acb'
S1 = Solution()
print(S1.Permutation(ss))

S2 = Solution1()
print(S2.Permutation(ss))
