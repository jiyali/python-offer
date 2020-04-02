# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间


class ListNode:
    def __init__(self, key=None, value=None):
        self.value = value
        self.key = key
        self.next = None
        self.pre = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}
        self.pre = None
        self.next = None

        # 建立双向链表
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def add_node_to_head(self, key, value):
        new = ListNode(key, value)
        self.hashmap[key] = new
        new.pre = self.head
        new.next = self.head.next

        self.head.next.pre = new
        self.head.next = new

    def move_node_to_head(self, key):
        node = self.hashmap[key]
        # 先把node拿出来
        node.pre.next = node.next
        node.next.pre = node.pre
        # 再把node放到开头
        node.pre = self.head
        node.next = self.head.next

        self.head.next.pre = node
        self.head.next = node

    def pop_tail(self):
        last_node = self.tail.pre
        self.hashmap.pop(last_node.key)
        last_node.pre.next = self.tail
        self.tail.pre = last_node.pre
        return last_node

    def get(self, key):
        if key in self.hashmap:
            self.move_node_to_head(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key, value):
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.move_node_to_head(key)
        else:
            if len(self.hashmap) >= self.capacity:
                self.pop_tail()
            self.add_node_to_head(key, value)







