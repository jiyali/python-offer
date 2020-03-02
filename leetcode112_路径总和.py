# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        self.res = False

        def dfs(root, path_sum = 0):
            if not root:
                return
            if not root.left and not root.right and path_sum + root.val == sum:
                self.res = True
            dfs(root.left, path_sum + root.val)
            dfs(root.right, path_sum + root.val)

        dfs(root)
        return self.res