# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其自底向上的层次遍历为：
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def levelOrderBottom(self, root):
        res = []
        queue = [(root, 1)]

        while queue:
            node, depth = queue.pop(0)
            if node:
                if len(res) < depth :
                    res = [[]] + res
                res[-depth].append(node.val)
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
        return res

