# 题目：给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，
#       并且它们的每个节点只能存储一位数字。
#       如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#       您可以假设除了数字 0 之外，这两个数都不会以 0 开头。


class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution(object):
    def addTwoNumber(self, l1, l2):
        # 累加获得第一个链表的数字和
        a, one = 0, 0
        while l1:
            a += l1.val * (10 ** one)
            one += 1
            l1 = l1.next

        b, two = 0, 0
        while l2:
            b += l2.val * (10 ** two)
            two += 1
            l2 = l2.next

        Sum = list(str(a + b))[::-1]

        temp = ListNode(None)
        node = ListNode(None)

        for i in Sum:
            if temp.val is None:
                temp = ListNode(i)
                node = temp
            else:
                temp.next = ListNode(i)
                temp = temp.next
        return node