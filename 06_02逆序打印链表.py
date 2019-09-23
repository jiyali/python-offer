# 思路二：使用递归，每访问一个节点，递归输出它后面的节点，再输出节点本身
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution(object):
    def printList(self, listnode):
        if listnode:
            self.printList(listnode.next)
            print(listnode.data)


node1 = Node(11)
node2 = Node(13)
node3 = Node(15)
node1.next = node2
node2.next = node3
s1 = Solution()
print(s1.printList(node1))
