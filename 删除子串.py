# 编写一个程序，当在一个字符串中出现子串时就删除它。
#  find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，
#  则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。


class Solution:
    def dele_substr(self, s1, s2):
        start_location = s1.find(s2)
        length = len(s2)
        res = s1[:start_location]+s1[start_location+length:]
        return res


s = Solution()
print(s.dele_substr(s1="abcdefgh", s2="cd"))
