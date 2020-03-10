# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
#
# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
#
# 示例 1:
#
# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 1


class TreeNode:
    def __init(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def kthSmallest(self, root, k):
        self.res = []

        def helper(root):
            if not root:
                return None
            helper(root.left)
            self.res.append(root.val)
            helper(root.right)
            return self.res

        helper(root)
        return self.res[k - 1]
