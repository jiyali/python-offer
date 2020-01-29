# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中没有重复出现的数字。


class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return None

        pre = pre_head = ListNode(None)
        pre.next = head
        cur = head

        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur:
                pre = cur
            cur = cur.next
            pre.next = cur
        return pre_head.next
