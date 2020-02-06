# 请判断一个链表是否为回文链表。


class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class Solution:
    def isPalindrome(self, head):
        pre_head = ListNode(0)
        pre_head.next = head
        slow = fast = pre_head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        pre = None
        cur = slow.next
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        a = pre_head.next
        b = pre
        while b:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        return True