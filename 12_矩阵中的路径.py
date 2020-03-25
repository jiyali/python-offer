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
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def exist(self, board, word):
        row = len(board)
        col = len(board[0])
        visited = [[0] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    if self.backtrack(i, j, visited, board, word[1:]):
                        return True
                    else:
                        visited[i][j] = 0
        return False

    def backtrack(self, i, j, visited, board, word):
        if len(word) == 0:
            return True
        for direc in self.directions:
            cur_i = i + direc[0]
            cur_j = j + direc[1]
            if 0 <= cur_i < len(board) and 0 <= cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                if visited[cur_i][cur_j] == 1:
                    continue
                visited[cur_i][cur_j] = 1
                if self.backtrack(cur_i, cur_j, visited, board, word[1:]) == True:
                    return True
                else:
                    visited[cur_i][cur_j] = 0
        return False


s = Solution()
print(s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
