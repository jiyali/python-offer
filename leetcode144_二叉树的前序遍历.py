# 给定一个二叉树，返回它的 前序 遍历。

# 迭代


class Solution:
    def preorderTraversal(self, root):
        res = []
        stack = []
        p = root
        while p or stack:
            while p:
                res.append(p.val)
                stack.append(p)
                p= p.left
            p = stack.pop().right
        return res

# 递归

class Solution:
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

