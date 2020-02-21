# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。


class Solution:
    def topKFrequent(self, nums, k):
        dic = {}
        res = []

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        dic = sorted(list(dic.items()), key=lambda x: x[1], reverse=True)

        for i in range(k):
            res.append(dic[i][0])
        return res
