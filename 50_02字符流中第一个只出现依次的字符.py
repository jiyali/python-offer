# 题目：请实现一个函数，用来找出字符流中第一个只出现一次的字符。
#       例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"；
#       当从 该字符流中读出前6个字符"google"时，第一个只出现一次的字符是"l"。


class Solution(object):
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.dic = {}

    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.dic[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        # write code here
        self.s += char
        if char not in self.dic:
            self.dic[char] = 1
        else:
            self.dic[char] += 1
