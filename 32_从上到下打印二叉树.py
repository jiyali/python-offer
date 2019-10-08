# 题目：从上往下打印出二叉树的每个节点，同层节点从左至右打印。

class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

    def PrintFromToBottom(self, root):
