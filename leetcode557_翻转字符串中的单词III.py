# 题目：给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。


class Solution(object):
    def reverseWords(self, s):
        if not s:
            return None
        temp = s.split(' ')
        return temp[::-1][::-1]
