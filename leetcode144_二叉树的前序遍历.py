# 给定一个二叉树，返回它的 前序 遍历。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 迭代
    def preorderTraversal(self, root):
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res


class Solution1:
    # 递归
    def preorderTraversal(self, root):
        res = []

        def helper(root):
            if not root:
                return None
            res.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return res

