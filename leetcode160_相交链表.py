# 编写一个程序，找到两个单链表相交的起始节点。


class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class Solution:
    def getIntersectionNode(self, headA, headB):
        a = headA
        b = headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
