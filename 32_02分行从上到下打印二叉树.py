# 题目：从上到下按层打印二叉树，同一层的节点按照从左到右的顺序打印，每一层打印到一行


class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def BranchesPrintFromTopToBottom(self, pRoot):
        if pRoot is None:
            return []

        nodes = [pRoot]
        output = []

        while nodes:
            currentStack = []
            nextStack = []

            for node in nodes:
                currentStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            output.append(currentStack)
            nodes = nextStack
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
aList = S.BranchesPrintFromTopToBottom(pNode1)
print(aList)
