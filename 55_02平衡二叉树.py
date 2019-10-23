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


pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)
pNode7 = TreeNode(7)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.right = pNode6
pNode5.left = pNode7

s = Solution()
print(s.IsBalanced_Solution(pNode1))
