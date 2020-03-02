# 计算给定二叉树的所有左叶子之和。
#
# 示例：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        self.res = 0

        def dfs(root):
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                self.res += root.left.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res