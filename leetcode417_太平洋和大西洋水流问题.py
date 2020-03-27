# 给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。
#
# 规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。
#
# 请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。
#
#  
#
# 提示：
#
# 输出坐标的顺序不重要
# m 和 n 都小于150
#  
#
# 示例：
#
#  
#
# 给定下面的 5x5 矩阵:
#
#   太平洋 ~   ~   ~   ~   ~
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * 大西洋
#
# 返回:
#
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row = len(matrix)
        col = len(matrix[0])
        res1 = set()
        res2 = set()

        def dfs(i, j, res):
            res.add((i, j))
            for dx, dy in directions:
                cur_i = i + dx
                cur_j = j + dy
                if 0 <= cur_i < row and 0 <= cur_j < col and matrix[i][j] <= matrix[cur_i][cur_j] and (
                cur_i, cur_j) not in res:
                    dfs(cur_i, cur_j, res)

        # 流入太平洋
        for i in range(row):
            dfs(i, 0, res1)
        for j in range(col):
            dfs(0, j, res1)
        # 流入大西洋
        for i in range(row):
            dfs(i, col - 1, res2)
        for j in range(col):
            dfs(row - 1, j, res2)
        return res1 & res2


s = Solution()
print(s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
