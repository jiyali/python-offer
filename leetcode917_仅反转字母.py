# 题目：给定一个字符串 S，返回 “反转后的” 字符串，
#       其中不是字母的字符都保留在原地，而所有字母的位置发生反转。


class Solution(object):
    def reverseOnlyLetters(self, s):
        letters = [c for c in s if c.isalpha()]
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)


s = Solution()
print(s.reverseOnlyLetters('a,b!rgh%'))
