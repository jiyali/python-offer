# 二维数组查找指定数字
# 思路：如果要查找的数字不在数组的右上角，则每次都在数组的查找范围中剔除一行或一列，这样就可以缩小查找范围，
#       知道找到查找数字或者查找范围为空


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here

        if not array:
            return False

        row = 0
        col = len(array[0]) - 1

        while row <= len(array) - 1 and col >= 0:
            if array[row][col] == target:
                return True
            elif array[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


s = Solution()
print(s.Find(array=[[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], target=2))
