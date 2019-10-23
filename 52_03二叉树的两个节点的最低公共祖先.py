# 题目：给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#      百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
#      满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”


class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.ans = None  # 存储公共祖先

    def lowestCommonAncestor(self, root, p, q):

        def recurse_tree(current_node):
            if not current_node:
                return False

            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)

            mid = current_node == p or current_node == q

            if mid + left + right >= 2:
                self.ans = current_node

            return mid or left or right

        recurse_tree(root)
        return self.ans


pNode1 = TreeNode(3)
pNode2 = TreeNode(5)
pNode3 = TreeNode(1)
pNode4 = TreeNode(6)
pNode5 = TreeNode(2)
pNode6 = TreeNode(0)
pNode7 = TreeNode(8)
pNode8 = TreeNode(7)
pNode9 = TreeNode(4)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7
pNode5.left = pNode8
pNode5.right = pNode9

S = Solution()
print(S.lowestCommonAncestor(pNode1, pNode2, pNode3))

