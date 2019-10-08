# 题目：请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
# 思路：前序遍历二叉树存入第一个序列中，
#       将前序遍历的序列按照父节点、右子节点、左子节点的顺序存入第二个序列中，
#       对比两个序列即可


class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetrical(self, pRoot):
        preList = self.preOrder(pRoot)
        mirrorList = self.mirrorPreOrder(pRoot)

        if preList == mirrorList:
            return True
        return False

    def preOrder(self, pRoot):
        if pRoot is None:
            return None

        treestack = []
        output = []
        pNode = pRoot

        while pNode or len(treestack) > 0:
            while pNode:
                treestack.append(pNode)
                output.append(pNode.val)
                pNode = pNode.left
                if not pNode:
                    output.append(None)
            if len(treestack):
                pNode = treestack.pop()
                pNode = pNode.right
                if not pNode:
                    output.append(None)
        return output

    def mirrorPreOrder(self, pRoot):
        if pRoot is None:
            return None

        treestack = []
        output = []
        pNode = pRoot

        while pNode or len(treestack) > 0:
            while pNode:
                treestack.append(pNode)
                output.append(pNode.val)
                pNode = pNode.right
                if not pNode:
                    output.append(None)
            if len(treestack):
                pNode = treestack.pop()
                pNode = pNode.left
                if not pNode:
                    output.append(None)
        return output


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
result = S.isSymmetrical(pNode1)
print(result)
