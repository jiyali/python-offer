# 题目：编写一个函数来查找字符串数组中的最长公共前缀。
#       如果不存在公共前缀，返回空字符串 ""。
"""
nums = ['flower','flow','flight']
for i in zip(*nums):
    print(i)

输出结果：

('f', 'f', 'f')
('l', 'l', 'l')
('o', 'o', 'i')
('w', 'w', 'g')
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        s = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s
