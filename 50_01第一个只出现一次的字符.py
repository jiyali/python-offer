# 题目：在字符串中找出第一个只出现一次的字符。如输入'abaccdeff'，则输出'b'


class Solution(object):
    def FirstNotRepeatingChar(self, s):
        if len(s) == 0:
            return -1

        dic = {}

        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i, val in enumerate(s):
            if dic[val] == 1:
                return i


s = Solution()
print(s.FirstNotRepeatingChar('abaccdeff'))
