# 题目：除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。


# 位操作
class Solution(object):
    def singleNumber(self, nums):
        a, b = 0, 0
        for i in nums:
            a = a ^ i & ~b
            b = b ^ i & ~a
        return a


# 思路二：通过这些不重复的元素和的三倍减去原来nums的和，得到的结果就是单个元素的两倍。
class Solution1(object):
    def singleNumber(self, nums):
        return (sum(set(nums)) * 3 - sum(nums)) // 2


# 思路三：哈希表
class Solution2(object):
    def singleNumber(self, nums):

        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for key in dic:
            if dic[key] == 1:
                return key


aList = [2, 2, 3, 2]
s = Solution2()
print(s.singleNumber(aList))
