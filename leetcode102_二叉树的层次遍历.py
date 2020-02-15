# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# 思路：每次出队列一个节点时，把他的孩子节点入队列


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def levelOrder(self, root):
        queue = [(root, 1)]
        res = []

        while queue:
            node, depth = queue.pop(0)
            if node:
                if depth > len(res):
                    res.append([])
                res[depth-1].append(node.val)
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
        return res
