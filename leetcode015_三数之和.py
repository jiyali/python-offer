# 题目：给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
#       找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。


class Solution(object):
    def threeSum(self, nums):
        dic = {}
        res = []

        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        pos = [i for i in dic if i > 0]
        neg = [i for i in dic if i < 0]

        neg.sort()

        if 0 in dic and dic[0] >= 3:
            res.append([0, 0, 0])
        for i in pos:
            for j in neg:
                k = -(i + j)
                if k in dic:
                    if j < k < i:
                        res.append([i, j, k])
                    elif (j == k or k == i) and dic[k] >= 2:
                        res.append([i, j, k])
                    if k < j:
                        break
        return res


