# 题目：在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
#       输入一个数组,求出这个数组中的逆序对的总数P。
#       例如，在数组{7,5,6,4}中，一共存在5个逆序对，分别是(7,6)(6,5)(5,4)(4,3)(3,2)(2,1)


# (不推荐)首先想到最笨的办法，估计这种方法面试会凉凉，时间复杂度O(n^2)
class Solution(object):
    def InversePairs(self, data):
        if len(data) < 2:
            return 0
        res = 0
        for i in range(len(data)-1):
            for j in range(i, len(data)):
                if data[i] > data[j]:
                    res += 1
        return res


# 归并排序，时间复杂度O(nlogn)
class Solution1(object):
    def __init__(self):
        self.res = 0

    def InversePairs(self, data):
        self.merge_sort(data)
        return self.res % 1000000007

    def merge_sort(self, data):
        if len(data) <= 1:
            return data
        s = 0
        e = len(data)
        mid = s + (e - s + 1) // 2
        list1 = self.merge_sort(data[s:mid])
        list2 = self.merge_sort(data[mid:e])
        data = self.merge(list1, list2)
        return data

    def merge(self, list1, list2):
        data = []
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] > list2[j]:
                self.res += (len(list2)-j)
                data.append(list1[i])
                i += 1
            else:
                data.append(list2[j])
                j += 1
        while i < len(list1):
            data.append(list1[i])
            i += 1
        while j < len(list2):
            data.append(list2[j])
            j += 1
        return data


class Solution2(object):
    def InversePairs(self, data):
        if len(data) <= 0:
            return 0
        count = 0
        copy = []
        for i in range(len(data)):
            copy.append(data[i])
        copy.sort()
        i = 0
        while len(copy) > i:
            count += data.index(copy[i])
            data.remove(copy[i])
            i += 1
        return count


s = Solution1()
print(s.InversePairs([1, 2, 3, 4, 5, 6, 0]))
