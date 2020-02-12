# 迭代

class Solution:
    def postorderTraversal(self,root):
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res

# 递归

class Solution:
    def postorderTraversal(self, root):
        res = []
        def helper(root):
            if not root:
                return None
            helper(root.left)
            helper(root.right)
            res.append(root.val)
        helper(root)
        return res