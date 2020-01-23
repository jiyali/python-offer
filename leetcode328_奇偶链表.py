# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。
# 请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，
# nodes 为节点总数


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def oddEvenList(self, head):
        odd = odd_head = ListNode(0)
        even = even_head = ListNode(0)
        flag = -1

        while head:
            if flag == -1:
                odd.next = head
                head = head.next
                odd = odd.next
                odd.next = None
            else:
                even.next = head
                head = head.next
                even = even.next
                even.next = None
            flag *= -1
        odd.next = even_head.next
        return odd_head.next



