"""方法功能：判断s2是否为s1的子串，如果是，那么返回s2在s1中第一次出现的下标，否则返回-1
　　输入参数：s1和s2分别为主串和模式串"""


class Solution:
    def BFSearch(self, s1, s2):
        l1 = len(s1)
        l2 = len(s2)
        i = j = 0
        while i < l1 and j < l2:
            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0
        if j == l2:
            return i - l2
        return -1


s = Solution()
print(s.BFSearch(s1='abcabdabceabd', s2='abce'))
