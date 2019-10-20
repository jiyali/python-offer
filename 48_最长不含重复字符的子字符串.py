# 题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
#       假设字符串中只包含从’a’到’z’的字符。


# 思路：滑动窗口，时间复杂度O(n)
class Solution(object):
    def longestSubstringWithoutDuplication(self, s):
        if not s or len(s) == 0:
            return 0

        left = 0
        lookup = set()

        max_len = 0
        cur_len = 0

        for i in range(len(s)):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len


# 思路二：利用哈希表
class Solution1(object):
    def longestSubstringWithoutDuplication(self, s):

        dict = {}
        start = 0
        cur_len = 0
        max_len = 0

        for i in range(len(s)):
            if s[i] in dict and dict[s[i]] >= start:
                start = dict[s[i]]+1
            dict[s[i]] = i  # 修改字典
            cur_len = i - start + 1
            if cur_len > max_len:
                max_len = cur_len
        return max_len


s = Solution1()
print(s.longestSubstringWithoutDuplication('arabcacfr'))


