# 题目：给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。


class TreeNode(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


class Solution(object):
    def isValidBST(self, root):
        res = []

        def helper(root):
            if not root:
                return None
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res == sorted(res) and len(set(res)) == len(res)

    def isValidBST1(self, root: TreeNode) -> bool:
        if not root:
            return True

        def helper(root, Min=float('-inf'), Max=float('inf')):
            if not root:
                return True
            if root.val <= Min or root.val >= Max:
                return False
            return helper(root.left, Min, root.val) and helper(root.right, root.val, Max)

        return helper(root)


pNode1 = TreeNode(2)
pNode2 = TreeNode(1)
pNode3 = TreeNode(3)

pNode1.left = pNode2
pNode1.right = pNode3


s = Solution()
print(s.isValidBST(pNode1))
