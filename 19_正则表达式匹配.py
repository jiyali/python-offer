# 题目：请实现一个函数用来匹配包含'.'和''的正则表达式。
#       模式中的字符'.'表示任何一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
#       在本题中，匹配指字符串的所有字符匹配整个模式。
#       例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。


class Solution(object):
    def match(self, s, pattern):
        # 如果s和pattern都为空，那么匹配
        if len(s) == 0 and len(pattern) == 0:
            return True
        # 如果s不为空，pattern为空，不匹配
        if len(s) > 0 and len(pattern) == 0:
            return False
        # 如果s为空，pattern不为空，那么如果pattern的第二个字符为 '*' 的话，继续递归匹配pattern第二个字符后面的字符
        if len(s) == 0 and len(pattern) > 0:
            if len(pattern) > 1 and pattern[1] == '*':
                return self.match(s, pattern[2:])
            else:
                return False
        # 如果s与pattern都不为空的话，
        if len(s) > 0 and len(pattern) > 0:
            if len(pattern) > 1 and pattern[1] == '*':
                # 如果s的第一个字符和pattern的第一个字符不相同，而且pattern的第一个字符不是'.'时，只能对比第三个字符之后的字符串
                if s[0] != pattern[0] and pattern[0] != '.':
                    return self.match(s, pattern[2:])
                else:
                    # 有三种情况：
                    # 第一种：pattern第二个字符'*'表示前面的字符出现0次，递归对比s和pattern的第三个字符开始的字符串
                    # 第二种：pattern第二个字符'*'表示前面的字符出现1次，递归对比s的第二个字符和pattern的第三个字符以后的字符串
                    # 第三种：pattern第二个字符'*'表示前面的字符出现多次，递归对比s的第二个字符和pattern的第一个字符以后的字符串
                    return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            else:
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.match(s[1:], pattern[1:])
                else:
                    return False