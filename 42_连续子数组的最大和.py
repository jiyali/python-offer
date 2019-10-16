# 题目：HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
#       今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
#       但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
#       例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
#       给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
#       输入一个整型数组,数组里有整数也有负数。数组中一二或连续的多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)

# 思路一：初始化和为0，从数组的第一个数开始累加，如果和小于0，则返回初始化的和，从下一个数开始继续累加，最后返回累加和中的最大值


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array is None or len(array) == 0:
            return []

        tmp = 0
        tmp_sum = []

        for i in array:
            tmp += i
            tmp_sum.append(tmp)

            if tmp > 0:
                continue
            else:
                tmp = 0
        return max(tmp_sum)


# 思路二：动态规划，初始化和为0，如果前i-1数的和小于0，则返回第i个值，如果前i-1个数的和大于0，则返回前i-1个数的和
class Solution1(object):
    def FindGreatestSumOfSubArray(self, array):
        if array is None or len(array) <= 0:
            return []

        tmp_sum = [0] * len(array)

        for i in range(len(array)):
            if i == 0 or tmp_sum[i-1] <= 0:
                tmp_sum[i] = array[i]
            else:
                tmp_sum[i] = tmp_sum[i-1] + array[i]

        return max(tmp_sum)


alist = [1, -2, 3, 10, -4, 7, 2, -5]
s = Solution1()
print(s.FindGreatestSumOfSubArray(alist))
