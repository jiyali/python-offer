class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution:
    def sort_alternating(self, head):
        if head is None:
            return None

        odd_head = odd_h = ListNode(0)
        even_head = even_h = ListNode(0)

        odd = head
        even = head.next

        while odd:
            odd_h.next = ListNode(odd.val)
            odd = odd.next.next if odd.next else None
            odd_h = odd_h.next

        while even:
            even_h.next = ListNode(even.val)
            even = even.next.next if even.next else None
            even_h = even_h.next

        prev = None
        odd_head = odd_head.next
        even_head = even_head.next
        while even_head:
            even_head.next, prev, even_head = prev, even_head, even_head.next

        ans = h = ListNode(0)
        while odd_head and prev:
            if odd_head.val <= prev.val:
                h.next = odd_head
                odd_head = odd_head.next
            else:
                h.next = prev
                prev = prev.next
            h = h.next
        h.next = odd_head or prev
        return ans.next


node1 = ListNode(1)
node2 = ListNode(8)
node3 = ListNode(3)
node4 = ListNode(6)
node5 = ListNode(5)
node6 = ListNode(4)
node7 = ListNode(7)
node8 = ListNode(2)
node9 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9

s = Solution()
print(s.sort_alternating(node1).next.val)
