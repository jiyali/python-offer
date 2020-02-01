# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。


class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class Solution:
    def reverseKGroup(self, head, k):
        # 如果没有要求空间复杂度时，可以用构造栈的方式
        pre = pre_head = ListNode(0)

        while True:
            stack = []
            count = k
            tmp = head
            while tmp and count:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            # 如果构不成k个，退出循环
            if count:
                pre.next = head
                break
            # 出栈，构成翻转
            while stack:
                pre.next = stack.pop()
                pre = pre.next
            # 与剩下的节点相连
            pre.next = tmp
            head = tmp
        return pre_head.next

