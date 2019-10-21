# 题目：删除字符串中重复的字符，例如，”good”去掉重复的字符串后就变成”god”

class Solution(object):
    def removeDuplicate(self, s):
        if len(s) == 0:
            return None

        alist = []

        for i in s:
            if i not in alist:
                alist.append(i)
        return ''.join(alist)


s = Solution()
print(s.removeDuplicate('good'))
