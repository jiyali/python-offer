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
    def InversePairs(self, data):
        return self.MergeSort(data[:], 0, len(data)-1, data[:]) % 1000000007

    def MergeSort(self, temp, left, right, data):
        if right - left < 1:
            return 0
        if right - left == 1:
            if data[left] < data[right]:
                return 0
            else:
                temp[left], temp[right] = data[right], data[left]
                return 1

        mid = left + (right - left + 1) // 2
        res = self.MergeSort(data, left, mid, temp) + self.MergeSort(data, mid + 1, right, temp)

        # 合
        i = left
        j = mid + 1
        index = left

        while i <= mid and j <= right:
            if data[i] <= data[j]:
                temp[index] = data[i]
                i += 1
            else:
                temp[index] = data[j]
                res += mid - i + 1
                j += 1
            index += 1
        while i <= mid:
            temp[index] = data[i]
            i += 1
            index += 1
        while j <= right:
            temp[index] = data[j]
            j += 1
            index += 1
        return res


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
