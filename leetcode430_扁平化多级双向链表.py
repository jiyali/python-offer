# 您将获得一个双向链表，除了下一个和前一个指针之外，它还有一个子指针，可能指向单独的双向链表。
# 这些子列表可能有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。
# 扁平化列表，使所有结点出现在单级双链表中。您将获得列表第一级的头部。
# 输入:
#  1---2---3---4---5---6--NULL
#          |
#          7---8---9---10--NULL
#              |
#              11--12--NULL
#
# 输出:
# 1-2-3-7-8-11-12-9-10-4-5-6-NULL


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head):
        if not head:
            return None

        pre = pre_head = Node(0, None, head, None)

        stack = []
        stack.append(head)

        while stack:
            cur = stack.pop()
            pre.next = cur
            cur.prev = pre

            if cur.next:
                stack.append(cur.next)

            if cur.child:
                stack.append(cur.child)
                cur.child = None
            pre = cur
        pre_head.next.prev = None
        return pre_head.next

