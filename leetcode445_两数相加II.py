# 给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。
# 它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。


class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class Solution:
    def addTwoNumbers(self, l1, l2):
        s1 = ''
        while l1:
            s1 += str(l1.val)
            l1 = l1.next

        s2 = ''
        while l2:
            s2 += str(l2.val)
            l2 = l2.next

        sum = list(str(int(s1) + int(s2)))

        temp_node = ListNode(None)
        node = ListNode(None)

        for i in sum:
            if temp_node.val is None:
                temp_node = ListNode(i)
                node = temp_node
            else:
                temp_node.next = ListNode(i)
                temp_node = temp_node.next
        return node
