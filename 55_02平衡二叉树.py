# 题目：输入一棵二叉树的根结点，判断该树是不是平衡二叉树。
#      如果某二叉树中任意结点的左右子树的深度相差不超过 1，那么它就是一棵平衡二叉树。


class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Solution(object):
    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True

        if abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) > 1:
            return False

        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0

        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)

        return max(left + 1, right + 1)
