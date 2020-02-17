# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回锯齿形层次遍历如下：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        queue = [(root, 1)]

        while queue:
            node, depth = queue.pop(0)
            if node:
                if depth > len(res):
                    res.append([])
                if depth & 1:
                    res[depth - 1].append(node.val)
                else:
                    res[depth - 1] = [node.val] + res[depth - 1]
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
        return res
