# 题目：输入两棵二叉树A，B，判断B是不是A的子结构。
#      （ps：我们约定空树不是任意一个树的子结构）


class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        flag = False
        if pRoot1 is not None and pRoot2 is not None:
            if pRoot1.val == pRoot2.val:
                flag = self.compare(pRoot1, pRoot2)
            if not flag:
                flag = self.HasSubtree(pRoot1.left, pRoot2)
            if not flag:
                flag = self.HasSubtree(pRoot1.right, pRoot2)
        return flag

    def compare(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.compare(pRoot1.left, pRoot2.left) and self.compare(pRoot1.right, pRoot2.right)


pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot8.left = pRoot9
pRoot8.right = pRoot10

S = Solution()
print(S.HasSubtree(pRoot1, pRoot8))
