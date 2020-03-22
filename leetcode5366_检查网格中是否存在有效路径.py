# 给你一个 m x n 的网格 grid。网格里的每个单元都代表一条街道。grid[i][j] 的街道可以是：
#
# 1 表示连接左单元格和右单元格的街道。
# 2 表示连接上单元格和下单元格的街道。
# 3 表示连接左单元格和下单元格的街道。
# 4 表示连接右单元格和下单元格的街道。
# 5 表示连接左单元格和上单元格的街道。
# 6 表示连接右单元格和上单元格的街道。
# 你最开始从左上角的单元格 (0,0) 开始出发，网格中的「有效路径」是指从左上方的单元格 (0,0) 开始、一直到右下方的 (m-1,n-1) 结束的路径。该路径必须只沿着街道走。
#
# 注意：你 不能 变更街道。
#
# 如果网格中存在有效的路径，则返回 true，否则返回 false 。


class Solution:
    def hasValidPath(self, grid):
        row = len(grid)
        col = len(grid[0])
        visit = [[0]*col for _ in range(row)]

        stack = []
        stack.append((0, 0))
        while stack:
            x, y = stack.pop()
            if x == row - 1 and y == col -1:
                return True

            # 向左
            if grid[x][y] in [1,3,5] and grid[x][y-1] in [1, 4, 6] and y-1 >=0 and visit[x][y-1] == 0:
                visit[x][y-1] = 1
                stack.append((x, y-1))

            # 向右
            if grid[x][y] in [1, 4, 6]and grid[x][y+1] in [1, 3, 5] and y+1<col and visit[x][y+1] == 0:
                visit[x][y+1] = 1
                stack.append((x, y+1))

            # 向上
            if grid[x][y] in [2,5, 6] and grid[x-1][y] in [2, 3, 4] and x-1>0 and visit[x-1][y]== 0:
                visit[x-1][y] = 1
                stack.append((x-1, y))

            # 向右
            if grid[x][y] in [2, 3, 4] and x + 1 < row and visit[x + 1][y] == 0 and grid[x + 1][y] in [2, 5, 6]:
                visit[x + 1][y] = 1
                stack.append((x + 1, y))
        return False


s = Solution()
print(s.hasValidPath([[2],[2],[2],[2],[2],[2],[6]]))