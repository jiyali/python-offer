# 给出一个完全二叉树，求出该树的节点个数。
#
# 说明：
#
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
#
# 示例:
#
# 输入:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# 输出: 6


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def countNodes(self, root):
        # 递归
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes1(self, root):
        # 深度优先搜索
        self.count = 0

        def dfs(root):
            if not root:
                return 0
            self.count += 1
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.count

# 二分判别的算法
    def countNodes2(self, root):
        if not root:
            return 0

        left = self.getdepth(root.left)
        right = self.getdepth(root.right)

        # 进行left==right上的判别处理
        if left == right:
            # 左子树为满二叉树
            return self.countNodes2(root.right) + (1 << left)
        else:
            # 没有右子树，可以直接计算出右子树的结点数量
            return self.countNodes2(root.left) + (1 << right)

    def getdepth(self, root):
        # 计算高度
        depth = 0
        while root:
            depth += 1
            root = root.left
        return depth
