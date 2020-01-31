# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class Solution:
    def swapPairs(self, head):
        pre = pre_head = ListNode(0)
        pre.next = head

        while head and head.next:
            a = head
            b = head.next
            pre.next = b
            a.next = b.next
            b.next = a
            pre = a
            head = a.next
        return pre_head.next
