# 题目：操作给定的二叉树，将其变换为源二叉树的镜像。
# 思路：遍历树，如果根节点存在子节点，则交换左右子节点的值（使用循环）


class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution(object):
    def Mirror(self, root):
        if root is None:
            return None

        stackNode = [root]

        while len(stackNode) > 0:
            nodeNum = len(stackNode) - 1
            tree = stackNode[nodeNum]
            stackNode.pop()
            nodeNum -= 1

            if tree.left is not None or tree.right is not None:
                tree.left, tree.right = tree.right, tree.left
            if tree.left:
                stackNode.append(tree.left)
                nodeNum += 1
            if tree.right:
                stackNode.append(tree.right)
                nodeNum += 1


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
S.Mirror(pNode1)
print(pNode1.right.left.val)
