# 题目：输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
#       路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
#       (注意: 在返回值的list中，数组长度大的数组靠前)


class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []

        if root.left is None and root.right is None:
            if expectNumber == root.val:
                return [[root.val]]
            else:
                return []

        stack = []

        leftStack = self.FindPath(root.left, expectNumber - root.val)
        rightStack = self.FindPath(root.right, expectNumber - root.val)

        for i in (leftStack + rightStack):
            stack.append([root.val] + i)

        return stack


pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)


pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5


S = Solution()
print(S.FindPath(pNode1, 22))
