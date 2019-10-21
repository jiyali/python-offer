# 题目：如果两个单词中出现的字母相同，并且每个字母出现的次数也相同，那么这两个单词互为变位词。
#      例如“silent”与“listen”，“evil”与“live”互为变位词。
#      请完成一个函数，判断输入的两个字符串是否互为变位词。


class Solution(object):
    def isAnagram(self, s1, s2):
        if len(s1) != len(s2):
            return False

        for i in set(s1):
            if s1.count(i) != s2.count(i):
                return False
        return True


s = Solution()
print(s.isAnagram('listen', 'silent'))
