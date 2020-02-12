#

# 迭代
class Solution:
    def inorderTraversal(self, root):
        res = []
        if not root:
            return None
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res


class Solution:
    def inorderTraversal(self, root):
        res = []
        def helper(root):
            if not root:
                return None
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res