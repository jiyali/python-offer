# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
# 你应当保留两个分区中每个节点的初始相对位置。


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def partition(self, head, x):
        left = left_head = ListNode(0)
        right = right_head = ListNode(0)

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next

        right.next = None
        left.next = right_head.next
        return left_head.next
