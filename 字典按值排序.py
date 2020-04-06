class Solution:
    def dicSort(self, dic):
        dic = sorted(dic.items(), key=lambda x: x[1])
        return dic


s = Solution()
print(s.dicSort({"a": 56, "b": 23, "f": 41, "c": 90, "d": 12, "e": 64, "g": 88}))
