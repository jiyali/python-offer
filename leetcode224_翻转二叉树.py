# 翻转一棵二叉树。
#
# 示例：
#
# 输入：
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 输出：
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# 栈模拟递归
# 时间复杂度：O(N)空间复杂度：O(NlogN)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.right)
                stack.append(node.left)
        return root
