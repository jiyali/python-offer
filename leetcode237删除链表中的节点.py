# 题目：请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。


class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node:
            return None

        tmpnode = node.next
        node.val = tmpnode.val
        node.next = tmpnode.next