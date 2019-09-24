class Solution:

    """
      输入矩阵：matrix
      矩阵行数：rows
      矩阵列数：cols
      要搜索的字符串：path
      当前行号：row
      当前列号：col
      已经处理的path中的字符个数：pathLength
    """

    def hasPath(self, matrix, rows, cols, path):
        if not matrix or rows < 1 or cols < 1 or not path:
            return False
        visited = [0] * (rows * cols)

        pathLength = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathLength, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, visited):
        if len(path) == pathLength:
            return True

        hasPath = False
        if not (not (0 <= row < rows) or not (0 <= col < cols) or not (matrix[row * cols + col] == path[pathLength]) or
                visited[row * cols + col]):

            pathLength += 1
            visited[row * cols + col] = True

            hasPath = self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathLength, visited)

            if not hasPath:
                pathLength -= 1
                visited[row * cols + col] = False

        return hasPath


s = Solution()
ifTrue = s.hasPath("ABCESFCSADEE", 3, 4, "ABCCED")
ifTrue2 = s.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", 5, 8, "SGGFIECVAASABCEHJIGQEM")
print(ifTrue)
print(ifTrue2)
