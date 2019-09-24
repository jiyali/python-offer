# 题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
#       路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
#       如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
#       例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
#       因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
# 思路：回溯法。任选一个格子作为路径的起点。
#       假设矩阵中某个格子的字符为ch并且这个格子将对应于路径上的第i个字符。
#       如果路径上的第i个字符不是ch，那么这个格子不可能处在路径上的第i个位置。
#       如果路径上的第i个字符正好是ch，那么往相邻的格子寻找路径上的第i+1个字符。
#       除在矩阵边界上的格子外，其他各自都有4个相邻的格子。重复这个过程直到路径上的所有字符都在矩阵中找到相应的位置。

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
        if 0 <= row < rows and 0 <= col < cols and matrix[row * cols + col] == path[pathLength] and not visited[row * cols + col]:

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
