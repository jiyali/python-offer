# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
# 示例:
#
# X X X X
# X O O X
# X X O X
# X O X X
# 运行你的函数后，矩阵变为：
#
# X X X X
# X X X X
# X X X X
# X O X X
# 解释:
#
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。


class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row = len(board)
        col = len(board[0])

        def dfs(i, j):
            board[i][j] = '0'
            for dx, dy in directions:
                cur_i = i + dx
                cur_j = j + dy
                if 0 <= cur_i < row and 0 <= cur_j < col and board[cur_i][cur_j] == 'O':
                    dfs(cur_i, cur_j)

        # 先查找最外层的O
        for i in range(row):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][col - 1] == 'O':
                dfs(i, col - 1)
        for j in range(col):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[row - 1][j] == 'O':
                dfs(row - 1, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '0':
                    board[i][j] = 'O'


s = Solution()
print(s.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
