# 题目：合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。


class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        length = len(lists)

        return self.merge(lists, 0, length - 1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]

        mid = left + (right - left) // 2

        list1 = self.merge(lists, left, mid)
        list2 = self.merge(lists, mid + 1, right)
        return self.mergeTwoLists(list1, list2)

    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
