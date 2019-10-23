# 题目：输入一棵二叉树的根结点，求该树的深度。
#       从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。


class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0

        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)

        if left > right:
            return left + 1
        else:
            return right + 1


pNode1 = TreeNode(5)
pNode2 = TreeNode(3)
pNode3 = TreeNode(7)
pNode4 = TreeNode(2)
pNode5 = TreeNode(4)
pNode6 = TreeNode(6)
pNode7 = TreeNode(8)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7
s = Solution()
print(s.TreeDepth(pNode1))