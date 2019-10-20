# 题目：我们把把只包含因子2、3和5的数称作丑数(Ugly Number)。
#       例如6、8都是丑数，但14不是，因为它包含因子7。
#       习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。


# 常规做法：计算每个数字是否能依次被2、3、5整除，整除后是否只剩1
class Solution(object):
    def GetUglyNumber_Solution(self, index):
        count = 1
        i = 1

        while count < index:
            i += 1
            if self.is_ugly(i):
                count += 1
        return i

    def is_ugly(self, num):
        while num % 2 == 0:
            num = num // 2
        while num % 3 == 0:
            num = num // 3
        while num % 5 == 0:
            num = num // 5
        return num == 1


# 上述方法。。有点慢。。不推荐
# 思路二：用空间换时间：将已经找到的丑数存在数组中，遍历数组查找即可
class Solution1(object):
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0

        ugly_list = [1]
        index_2 = 0
        index_3 = 0
        index_5 = 0

        for i in range(index-1):
            # print(index_2, index_3, index_5)
            new_ugly = min(ugly_list[index_2] * 2, ugly_list[index_3] * 3, ugly_list[index_5] * 5)
            # print(new_ugly)
            ugly_list.append(new_ugly)
            if new_ugly % 2 == 0:
                index_2 += 1
            if new_ugly % 3 == 0:
                index_3 += 1
            if new_ugly % 5 == 0:
                index_5 += 1

        return ugly_list[-1]


s = Solution1()
print(s.GetUglyNumber_Solution(1))
print(s.GetUglyNumber_Solution(1500))
