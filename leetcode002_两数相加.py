# 题目：给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，
#       并且它们的每个节点只能存储一位数字。
#       如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#       您可以假设除了数字 0 之外，这两个数都不会以 0 开头。


class ListNonde(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution(object):
    def addTwoNumber(self, l1, l2):
        if not l1 or not l2:
            return None

    def getNum(self, l):
        if l.next is None:
            return l.val
        return self.getNum((l.next) * 10 + l.val)

    def
