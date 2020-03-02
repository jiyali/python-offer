# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
# 示例 1:
#
# 给定二叉树 [3,9,20,null,null,15,7]
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def isBalanced(self, root):
        def rec(root):
            if not root:
                return True, 0

            is_banlance_l, depth_l = rec(root.left)
            is_banlance_r, depth_r = rec(root.right)

            is_banlance = is_banlance_l and is_banlance_r  and abs(depth_l - depth_r) <= 1
            depth = 1 + max(depth_l, depth_r)
            return (is_banlance, depth)
        return rec(root)[0]
