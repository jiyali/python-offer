# 思路：前序遍历的第一个值一定是根节点，中序遍历根节点所在位置的左面是左子树对应的子序列，
#       根节点位置右面的树右子树对应的子序列。再根据递归，继续构建左右子树。
class TreeNode(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self,preorder,inorder):
        if not preorder or not inorder:
            return False
        root = TreeNode(preorder[0])
        if set(preorder) != set(inorder): # 判断是否是同一颗二叉树
            return False
        index = inorder.index(preorder[0])
        # index() 函数用于从列表中找出某个值第一个匹配项的索引位置
        root.left = self.buildTree(preorder[1 : index + 1],inorder[:index])
        root.right = self.buildTree(preorder[index + 1 : ],inorder[index + 1 : ])
        return root

preorder = [1, 2, 3, 5, 6, 4]
inorder = [5, 3, 6, 2, 4, 1]
test = Solution()
newTree = test.buildTree(preorder, inorder)

def PrintNodeAtLevel(treeNode, level):
    if not treeNode or level < 0:
        return 0
    if level == 0:
        print(treeNode.data)
        return 1
    PrintNodeAtLevel(treeNode.left, level-1)
    PrintNodeAtLevel(treeNode.right, level-1)

print(PrintNodeAtLevel(newTree, 0))
