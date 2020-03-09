# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Soluton:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        idx = inorder.index(preorder[0])
        left = inorder[:idx]
        right = inorder[idx+1:]

        root.left = self.buildTree(preorder[1:idx+1], left)
        root.right = self.buildTree(preorder[idx+1:], right)

        return root
