# 题目：给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
#       百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
#       满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”


# 思路：根据二叉搜索树的特点，左子树都比根节点的值要小，右子树都比根节点的值要大，
#       利用递归的思路查找公共祖先时，1.从根节点开始遍历树
#                                   2.如果节点 pp 和节点 qq 都在右子树上，那么以右孩子为根节点继续 1 的操作
#                                   3.如果节点 pp 和节点 qq 都在左子树上，那么以左孩子为根节点继续 1 的操作
#                                   4.如果条件 2 和条件 3 都不成立，这就意味着我们已经找到节 pp 和节点 qq 的 LCA 了

class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p is None or q is None:
            return None

        if p == q:
            return None

        pval = p.val
        qval = q.val

        while root is not None:
            if pval < root.val and qval < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            elif pval > root.val and qval > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return root


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
print(S.lowestCommonAncestor(pNode3, pNode7, pNode1))
