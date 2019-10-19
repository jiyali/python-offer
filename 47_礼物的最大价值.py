# 题目：在一个mxn的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。
#       你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或 向下移动一格，知道到达棋盘的右下角。
#       给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？

# 思路：动态规划问题：假设当前在点(x,y)处，则当前得到的礼物价值和的最大值为f(i,j)=max(f(x-1,y),f(x,y-1))+g[i,j],
#       g[i,j]代表当前的礼物的价值


class Solution(object):
    def getMaxValue(self, grid):
        if len(grid) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        max_values = []
        for _ in range(len(grid)):
            max_values.append([0] * len(grid[0]))
        max_values[0][0] = grid[0][0]

        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0:
                    up = max_values[i-1][j]
                if j > 0:
                    left = max_values[i][j-1]
                max_values[i][j] = max(up, left) + grid[i][j]

        max_val = max_values[-1][-1]
        return max_val


s = Solution()
grid = [[2, 3, 1],
        [1, 7, 1],
        [4, 6, 1]]
print(s.getMaxValue(grid))
