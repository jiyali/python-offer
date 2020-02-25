# DFS + 队列
# 时间复杂度:O(N) 空间复杂度：O(1)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        queue = [(root, 1)]
        while queue:
            root,depth = queue.pop(0)
            if root:
                if root.left or root.right:
                    queue.append((root.left, depth + 1))
                    queue.append((root.right, depth + 1))
                else:
                    return depth
        return 0
