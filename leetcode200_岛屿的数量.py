# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
#
# 输出: 1


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        count = 0
        directins = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row = len(grid)
        col = len(grid[0])

        def dfs(grid, i, j):
            grid[i][j] = '0'
            for dx, dy in directins:
                cur_i = i + dx
                cur_j = j + dy
                if 0 <= cur_i < row and 0 <= cur_j < col and grid[cur_i][cur_j] == '1':
                    dfs(grid, cur_i, cur_j)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count


s = Solution()
print(s.numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
