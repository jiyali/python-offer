# 题目：输入一个链表，输出该链表中倒数第k个节点。
#      为了符合大多数人的习惯，本题从1开始计数，即链表的尾结点是倒数第一个节点。
#      例如，一个链表有6个节点， 从头节点开始，它们的值依次是1、2、3、4、5、6,。
#      这个链表的倒数第三个节点值为4


# 思路一：由于是单向链表，只能从头指针开始遍历，要想要到倒数k个节点，要先遍历一次链表，知道链表的长度，
#         然后输出n-k+1个节点的数值即可
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def FindKthToTail(self, head, k):
        if head is None:
            return None

        n = 1
        node = head

        while node.next is not None:
            n += 1
            node = node.next

        if k > n:
            return None
        for i in range(n - k):
            head = head.next

        return head


# 思路二： 如果只遍历一次链表的话，要定义两个指针，第一个指针先开始遍历，到遍历到k-1步后，第二个指针开始一起移动。


class Solution1(object):
    def FindKthToTail(self, head, k):
        if head is None or k <= 0:
            return None

        node1 = head
        node2 = None

        for i in range(k - 1):
            if node1.next is not None:
                node1 = node1.next
            else:
                return None
        node2 = head
        while node1.next is not None:
            node1 = node1.next
            node2 = node2.next
        return node2
