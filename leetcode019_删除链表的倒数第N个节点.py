# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。


class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class Solution:
    def removeNthFromEnd(self, head, n):
        if n == 0:
            return head

        pre = pre_head = ListNode(0)
        pre.next = head
        last = head

        while last:
            if n > 0:
                n -= 1
            else:
                pre = pre.next
            last = last.next

        pre.next = pre.next.next
        return pre_head.next
