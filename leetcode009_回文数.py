# 题目：判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。


class Solution(object):
    def isPalindrome(self, x):
        x = x.lstrip()
        if len(x) == 0:
            return 0

        if