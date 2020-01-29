# 删除链表中给定值val的所有节点


class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class Solution:
    def removeElements(self, head, val):
        if not head:
            return None

        pre = pre_head = ListNode(0)
        pre.next = head
        while head:
            if head.val == val:
                head = head.next
                pre.next = head
            else:
                pre = head
                head = head.next
        return pre_head.next