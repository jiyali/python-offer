# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。


class Solution:
    def lengthOfLongestSubstring(self,s):
        left = 0
        max_len = 0
        cur_len = 0
        lookup = set()

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


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
