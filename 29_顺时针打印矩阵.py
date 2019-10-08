# 题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
#      例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
#      则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if matrix is None:
            return None

        printArr = []

        rows = len(matrix)  # 行数
        cols = len(matrix[0])  # 列数
        start = 0

        while rows > start * 2 and cols > start * 2:
            endX = cols - 1 - start
            endY = rows - 1 - start

            # 从左到右打印一行
            for i in range(start, endX+1):
                number = matrix[start][i]
                printArr.append(number)

            # 从上到下打印一行
            if start < endY:
                for i in range(start+1, endY+1):
                    number = matrix[i][endX]
                    printArr.append(number)

            # 从右到左打印一行
            if start < endX and start < endY:
                for i in range(endX-1, start-1, -1):
                    number = matrix[endY][i]
                    printArr.append(number)

            # 从下到上打印一行
            if start < endX and start < endY-1:
                for i in range(endY-1, start, -1):
                    number = matrix[i][start]
                    printArr.append(number)

            start += 1
        return printArr


matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix2 = [[1], [2], [3], [4], [5]]
matrix3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
S = Solution()
print(S.printMatrix(matrix))
print(S.printMatrix(matrix2))
print(S.printMatrix(matrix3))
