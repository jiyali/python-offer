# 题目：字符串左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
#       比如，驶入字符串'abcdefg'和数字2，该函数返回左旋转两位得到的结果'cdefgab'


class Solution:
    def LeftRotateString(self, s, n):
        if s is None or len(s) == 0:
            return ''

        strList = list(s)
        strList = self.Reverse(strList)

        pivot = len(s) - n

        frontList = self.Reverse(strList[:pivot])
        behindList = self.Reverse(strList[pivot:])
        result = ''.join(frontList) + ''.join(behindList)
        return result

    def Reverse(self, alist):
        if alist is None or len(alist) == 0:
            return ''

        startIndex = 0
        endIndex = len(alist) - 1

        while startIndex < endIndex:
            alist[startIndex], alist[endIndex] = alist[endIndex], alist[startIndex]
            startIndex += 1
            endIndex -= 1
        return alist


str = 'abcdefg'
s = Solution()
print(s.Reverse(list('abcdefg')))
print(s.LeftRotateString(str, 2))
