# 题目：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
#       第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
# 思路：使用栈先入后出的特性打印，
#       如果当前打印的是奇数层，则保存它下一层节点时，先保存左子节点，再保存右子节点
#       如果当前打印的是偶数层，则保存它下一层节点时，先保存右子节点，在保存左子节点
#       以上两种情况的结果，分别保存在两个栈中


class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []

        nodes = [pRoot]
        output = []

        left_to_right = True

        while nodes:
            currentStack = []
            nextStack = []

            if left_to_right:
                for node in nodes:
                    currentStack.append(node.val)
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)
            else:
                for node in nodes:
                    currentStack.append(node.val)
                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)

            nextStack.reverse()
            left_to_right = not left_to_right
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
aList = S.Print(pNode1)
print(aList)