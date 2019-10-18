class Solution(object):
    def maxAreaOfIsland(self, grid):
        if grid is None or len(grid) == 0:
            return None
        if grid == [0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        vec = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 根据深度优先，见下示意图
        '''
                 x-1,y
           x,y-1  x,y    x,y+1
                x+1,y        
        '''
        res = 0

        for i in range(m):
            for j in range(n):
                # 判断当前节点是不是1，标记为0(不再重复)，继续搜索其他位置
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    ss = self.dfs(i, j, vec, grid)  # 因为是递归，每次count的数字是不同的。
                    res = max(res, ss)  # 很微妙。。比如前面如果遍历过的最大区域为3，再次遍历为2的话，要取最大
        return res

    def dfs(self, i, j, vec, grid):
        count = 1  # 在上一个循环里面已经判断过是符合条件的了，本身已经是1
        # 继续搜索下一个区域
        for dx, dy in vec:
            nx, ny = i + dx, j + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                grid[nx][ny] = 0
                count += self.dfs(nx, ny, vec, grid)
        return count


grid = [[1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1]]

solution = Solution()
result = solution.maxAreaOfIsland(grid)
print(result)
