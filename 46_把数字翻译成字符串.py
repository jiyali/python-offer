# 题目：给定一个数字，我们按照如下规则把它翻译为字符串；0翻译成“a”，1翻译成“b”,… 11翻译成“l”,…,25翻译成“z”.
#      一个数字可能有多个翻译。例如，12258有5种不同的翻译， 分别是“bccfi” “bwfi” “bczi” “mcfi” “mzi”
#      请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

# 思路：循环去查每个数字是否能和他前一个数字组成一个能翻译的数字


class Solution(object):
    def getTranslationCount(self, s):
        if s is None or len(s) < 0:
            return ''

        means = [None] * len(s)  # 表示有多少种翻译方式
        means[0] = 1

        for i in range(1, len(s)):
            cur = means[i - 1]

            if 9 < int(s[i - 1:i + 1]) < 26:  # 9 < s[i-1] 和 s[i] 组成的数 < 26
                if i - 2 < 0:  # 两位数字只能累加1 比如11~25
                    cur += 1
                else:  # 三位以上开始累加之前位数所有的可能性
                    cur += means[i - 2]
            means[i] = cur

        return means[len(s) - 1]


s = Solution()
print(s.getTranslationCount("1225825"))
