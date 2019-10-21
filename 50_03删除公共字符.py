# 题目：输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。
#      例如，输入”They are students.”和”aeiou”，则删除之后的第一个字符串变成”Thy r stdnts.”


class Solution(object):
    def DeleCommonChar(self, s1, s2):
        s1 = input()
        s2 = input()

        for i in s2:
            s1 = s1.replace(i, '')
        return s1


s = Solution()
print(s.DeleCommonChar("They are students.", "aeiou"))


