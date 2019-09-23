# 思路：中序遍历的顺序是 左子节点 → 根节点 → 右子节点。
#       如果一棵树存在右子树，那么下一个节点一定是右子树的左节点
#       如果不存在右子树，如果存在左子节点，下一个节点是父节点
#                        如果存在右子节点，沿这个节点的父节点向上遍历，直到找到一个节点是其父节点的左子节点，则下一个节点就是这个节点的父节点
class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def getnext(self, pnode):
        if not pnode:
            return None

        if pnode.right:
            pnode = pnode.right
            while pnode.left:
                pnode = pnode.left
            return pnode
        else:
            while pnode.next:
                if pnode == pnode.next.left:
                    return pnode.next
                pnode = pnode.next
            return None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.insertLeft = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(9)

s = Solution()

print(s.getnext(root).data)
