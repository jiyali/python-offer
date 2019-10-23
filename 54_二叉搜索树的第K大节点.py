# 题目：给定一棵二叉搜索树，请找出其中的第k小的结点。
#      例如（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4

# 思路：由于二叉搜索树的特性，从小到大排列的话要使用中序遍历，中序遍历输出一个序列后找到序列中第k个数即可。
class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution(object):
    # 返回对应节点TreeNode
    def __init__(self):
        self.alist = []

    def KthNode(self, pRoot, k):
        if not pRoot or k <= 0:
            return None

        self.inorder_traversal(pRoot)

        if len(self.alist) < k:
            return None
        else:
            return self.alist[k - 1]

    def inorder_traversal(self, pRoot):
        if pRoot is None:
            return None
        self.inorder_traversal(pRoot.left)
        self.alist.append(pRoot)
        self.inorder_traversal(pRoot.right)


pNode1 = TreeNode(5)
pNode2 = TreeNode(3)
pNode3 = TreeNode(7)
pNode4 = TreeNode(2)
pNode5 = TreeNode(4)
pNode6 = TreeNode(6)
pNode7 = TreeNode(8)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7
s = Solution()
print(s.KthNode(pNode1, 3).val)
