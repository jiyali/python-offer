class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def __init__(self, array):
        # 初始化链表
        self.count = 0
        if not array:
            self.head = None
        temp = None
        for i in array:
            if not temp:
                self.head = Node(i)
                temp = self.head
            else:
                temp.next = Node(i)
                temp = temp.next
            self.count += 1

    def series(self, head):
        # 把链表按照题目要求输出
        if not head:
            return None
        res = []
        temp = head
        while temp:
            res.append(temp.val)
            temp = temp.next
        print(' '.join(map(str, res)))

    def k_reverse(self, head, k):
        # 链表按照每k节点反转一次，思路是每K个节点生成首尾的指针，然后按照首尾指针进行K个节点的翻转
        # 每次翻转后的尾节点连向下一段节点，
        # 其中下一段节点通过递归的方式来生成
        if head == None:
            return head
        cur = head
        for i in range(k - 1):
            cur = cur.next
            if cur == None:
                return head
        next = cur.next
        cur = self.reverse(head, cur)
        head.next = self.k_reverse(next, k)
        return cur

    def reverse(self, head, tail):
        # k_reverse的局部函数，用于给定首尾节点进行翻转
        if head == None:
            return None
        cur = head
        pre = None
        post = None
        while cur != tail:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
        cur.next = pre
        return cur


def main():
    # 先获取输入
    # 把输入初始化为链表
    # 让链表每K个翻转一次
    # 输出链表
    in_list = map(int, input().split(" "))
    k = int(input())
    s = Solution(in_list)
    new_head = s.k_reverse(s.head, k)
    s.series(new_head)


main()