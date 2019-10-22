# 题目：在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
#       输入一个数组,求出这个数组中的逆序对的总数P。
#       例如，在数组{7,5,6,4}中，一共存在5个逆序对，分别是(7,6)(6,5)(5,4)(4,3)(3,2)(2,1)


# (不推荐)首先想到最笨的办法，估计这种方法面试会凉凉，时间复杂度O(n^2)
class Solution(object):
    def InversePairs(self, data):
        if len(data) < 2:
            return 0
        res = 0
        for i in range(len(data) - 1):
            for j in range(i, len(data)):
                if data[i] > data[j]:
                    res += 1
        return res


# 归并排序，时间复杂度O(nlogn) 牛客上通过25%
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
        mid = s + (e + 1 - s) // 2

        left = self.merge_sort(data[:mid])
        # print('left= ', left)

        right = self.merge_sort(data[mid:])
        # print('right= ', right)

        data = self.merge(left, right)

        return data

    def merge(self, left, right):
        data = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                self.res += (len(left) - i)  # 比如[0,1,2,5,8][4,6,7,9] 当i=3时，5>4,5后面的数字都与4组成逆序关系
                # print('self.data=', self.res)
                data.append(right[j])
                # print('data1=', data)
                j += 1
            else:
                data.append(left[i])
                # print('data2=', data)
                i += 1
        while i < len(left):
            data.append(left[i])
            # print('data3=', data)
            i += 1
        while j < len(right):
            data.append(right[j])
            # print('data4=', data)
            j += 1
        return data


# 跟上述方法思想相同，但是通过75%
class Solution2(object):
    def __init__(self):
        self.res = 0

    def InversePairs(self, data):
        # write code here
        self.merge_sort(data)
        return self.res % 1000000007

    def merge_sort(self, data):
        if len(data) <= 1:
            return data

        start = 0
        end = len(data)
        mid = start + (end - start + 1) // 2

        left = self.merge_sort(data[start:mid])
        right = self.merge_sort(data[mid:end])

        data = self.merge(left, right)
        return data

    def merge(self, left, right):
        data = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                self.res += (len(right) - j)
                data.append(left[i])
                i += 1
            else:
                data.append(right[j])
                j += 1
        while i < len(left):
            data.append(left[i])
            i += 1
        while j < len(right):
            data.append(right[j])
            j += 1
        return data


# 根据数据的index，牛客通过50%
class Solution3(object):
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


s = Solution3()
print(s.InversePairs(
    [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366, 315, 301, 601, 650, 418, 355, 460, 505, 360,
     965, 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550, 474, 162, 268, 142,
     463, 221, 882, 576, 604, 739, 288, 569, 256, 936, 275, 401, 497, 82, 935, 983, 583, 523, 697, 478, 147, 795, 380,
     973, 958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630, 425, 930, 64, 266, 235, 187, 284, 665,
     874, 80, 45, 848, 38, 811, 267, 575]))
