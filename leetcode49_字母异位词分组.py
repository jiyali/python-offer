# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}

        for i in strs:
            key = ''.join(sorted(i))
            if key not in dic:
                dic[key] = [i]
            else:
                dic[key].append(i)
        return list(dic.values())

    def groupAnagrams1(self, strs):
        from collections import defaultdict
        # defaultdict属于内建函数dict的一个子类，调用工厂函数提供缺失的值
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        lookup = defaultdict(list)
        for _str in strs:
            key_val = 1
            for s in _str:
                key_val *= prime[ord(s) - 97]
            lookup[key_val].append(_str)
        return list(lookup.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.groupAnagrams1(["eat", "tea", "tan", "ate", "nat", "bat"]))
