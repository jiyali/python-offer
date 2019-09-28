# 题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
#       使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
#       并保证奇数和奇数，偶数和偶数之间的相对位置不变。


# 基本解法：遍历数组，遇到偶数，将偶数后面的数字依次前移，将偶数放到数组的最后位置，以此类推
#           方法比较烂，复杂度为O(n*n)
# 稍微改进的方法：设计两个数组，遍历数组，如果是奇数放入第一个数组中，如果是偶数放入第二个数组中


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