# 对链表进行插入排序。


class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class Solution:
    def insertionSortList(self, head):
        pre = pre_head = ListNode(0)
        pre.next = head
        cur = head

        while cur and cur.next:
            if cur.val <= cur.next.val:
                cur = cur.next
            else:
                tmp = cur.next
                cur.next = tmp.next
                pre = pre_head
                while pre.next.val <= tmp.val:
                    pre = pre.next
                tmp.next = pre.next
                pre.next = tmp
        return pre_head.next