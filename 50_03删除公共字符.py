# 题目：输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。
#      例如，输入”They are students.”和”aeiou”，则删除之后的第一个字符串变成”Thy r stdnts.”


class Solution(object):
    def DeleCommonChar(self, s1, s2):
        s1 = input()
        s2 = input()

        tmp = []
        ans = []
        for i in s1:
            if i not in s2:
                tmp.append(i)
        ans.append(''.join(tmp))

        return ' '.join(ans)


