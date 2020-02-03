# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cut = slow = fast = head
        while fast and fast.next:
            cut = slow
            fast = fast.next.next
            slow = slow.next
        cut.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)

    def merge(self, left, right):
        m = n = ListNode(0)
        while left and right:
            if left.val <= right.val:
                n.next = left
                left = left.next
            else:
                n.next = right
                right = right.next
            n = n.next
        n.next = left or right
        return m.next