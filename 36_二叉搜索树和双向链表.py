# 题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
#       要求不能创建任何新的结点，只能调整树中结点指针的指向。
# 思路：根据二叉搜索树的性质，如果想要转换成一个排序的序列，需要使用中序遍历。
#       要想转换成双向链表还不能创建新的节点，则只能调整所有的指针方向，
#       转换方法为：原先指向左子树的指针调整为前向指针(指向前一个节点)，原先指向右子节点的指针调整为后向指针(指向后一个节点)


class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None

        if pRootOfTree.left is None and pRootOfTree.right is None:
            return pRootOfTree

        # 将左子树转换为双向链表，返回链表头
        left = self.Convert(pRootOfTree.left)
        pLeft = left

        # 连接左子树和根节点
        if left is not None:
            while pLeft.right is not None:
                pLeft = pLeft.right
            pLeft.right = pRootOfTree
            pRootOfTree.left = pLeft

        # 将右子树转换成双向链表
        right = self.Convert(pRootOfTree.right)

        # 连接右子树和根节点
        if right:
            right.left = pRootOfTree
            pRootOfTree.right = right

        return left if left else pRootOfTree


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
newList = S.Convert(pNode1)
print(newList.val)
