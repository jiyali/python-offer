# 题目：输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
#       例如输入字符串"I am a student."，则输出"student . a am I"


class Solution(object):
    def ReverseSentence(self, s):
        if not s:
            return s
        l = s.split(' ')
        return ' '.join(l[::-1])


class Solution1(object):
    def ReverseSentence(self, s):
        if s is None or len(s) == 0:
            return s
        strList = list(s)
        strList = self.Reverse(strList)

        pBegin = 0
        pEnd = 0
        resultStr = ''
        listtmp = []

        while pEnd < len(s):
            if pEnd == len(s) - 1:
                listtmp.append(self.Reverse(strList[pBegin:]))
                break

            if strList[pBegin] == ' ':
                pBegin += 1
                pEnd += 1
                listtmp.append(' ')
            elif strList[pEnd] == ' ':
                listtmp.append(self.Reverse(strList[pBegin:pEnd]))
                pBegin = pEnd
            else:
                pEnd += 1

        for i in listtmp:
            resultStr += ''.join(i)
        return resultStr

    def Reverse(self, alist):
        if alist is None or len(alist) == 0:
            return ''

        startIndex = 0
        endIndex = len(alist) - 1
        while startIndex < endIndex:
            alist[startIndex], alist[endIndex] = alist[endIndex],alist[startIndex]
            startIndex += 1
            endIndex -= 1
        return alist


str = 'I am a student.'
s = Solution1()
print(s.ReverseSentence(str))
