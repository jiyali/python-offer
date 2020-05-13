# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
# 示例:
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def rightSideView(self, root):
        queue = [(root, 0)]
        res = []

        while queue:
            node, depth = queue.pop(0)
            if node:
                if depth == len(res):
                    res.append(node.val)
                queue.append((node.right, depth + 1))
                queue.append((node.left, depth + 1))
        return res


class Solution1:
    def rightSideView(self, root):
        if not root:
            return None
        res = []

        def helper(root, depth=1):
            if not root:
                return None
            if depth > len(res):
                res.append(root.val)
            helper(root.right, depth + 1)
            helper(root.left, depth + 1)

        helper(root)
        return res
