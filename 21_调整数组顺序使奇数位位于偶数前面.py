# 题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
#       使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
#       并保证奇数和奇数，偶数和偶数之间的相对位置不变。


# 基本解法：遍历数组，遇到偶数，将偶数后面的数字依次前移，将偶数放到数组的最后位置，以此类推
#           方法比较烂，复杂度为O(n*n)
# 稍微改进的方法：设计两个数组，遍历数组，如果是奇数放入第一个数组中，如果是偶数放入第二个数组中
#           时间复杂度O(1),空间复杂度O(n)

class Solution(object):
    def reOrderArray(self, array):

        odd_list = []  # 奇数
        even_list = []  # 偶数

        for value in array:
            if value % 2 == 1:
                odd_list.append(value)
            else:
                even_list.append(value)
        return odd_list + even_list


S = Solution()
print(S.reOrderArray([-1, 2, -3, 4, -5, -6, 7, 8, 9, 10, -10]))

# 思路二：python双端队列
#         从前往后扫描数组的元素，如果是偶数，则append从右端添加元素。
#         从后往前扫描数组的元素，如果是奇数，则appendleft从左端添加元素。


from collections import deque


class Solution1(object):
    def reOrderArray(self, array):
        odd = deque()
        for i in range(len(array)):
            if array[i] % 2 == 0:
                odd.append(array[i])  # append() 从右端添加一个元素
            if array[len(array) - i - 1] % 2 == 1:
                odd.appendleft(array[len(array) - i - 1])  # appendleft() 从左端添加一个元素
        return list(odd)


S = Solution1()
print(S.reOrderArray([-1, 2, -3, 4, -5, -6, 7, 8, 9, 10, -10]))


# 思路三： 数组内互换的方法，
#         时间复杂度O(n*n)，空间复杂度O(1)


class Solution2(object):
    def reOrderArray(self, array):
        count = 0
        for i in range(len(array)):
            for j in range(len(array) - 1, i, -1):
                # print('here1')
                if array[j-1] % 2 == 0 and array[j] % 2 == 1:
                    array[j - 1], array[j] = array[j], array[j-1]
                    # print('here2')
                    # print(array)
        return array


S = Solution2()
print(S.reOrderArray([-1, 2, -3, 4, -5, -6, 7, 8, 9, 10, -10]))