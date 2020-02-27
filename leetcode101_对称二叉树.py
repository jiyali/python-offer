# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 递归判断左子树的左节点是否与右子树的右节点相同
# 时间复杂度O(N),空间复杂度O(N))
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.Symmetric(root, root)

    def Symmetric(self, lef, righ):
        if not righ and not lef:
            return True
        elif not righ or not lef:
            return False
        elif lef.val != righ.val:
            return False
        return self.Symmetric(lef.left, righ.right) and self.Symmetric(lef.right, righ.left)