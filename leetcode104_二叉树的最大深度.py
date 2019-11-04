# 题目：给定一个二叉树，找出其最大深度。
#       二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#       说明: 叶子节点是指没有子节点的节点。


class TreeNode(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


class Solution(object):
    # 递归算法
    def maxDepth(self, root):
        if not root:
            return 0

        else:
            left_deep = self.maxDepth(root.left)
            right_deep = self.maxDepth(root.right)
        return max(left_deep, right_deep) + 1