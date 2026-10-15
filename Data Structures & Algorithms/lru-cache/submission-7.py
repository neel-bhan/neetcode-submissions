class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def push(self, node):
        temp = self.left.next
        self.left.next = node
        node.next = temp
        node.prev = self.left
        temp.prev = node

    def __init__(self, capacity: int):
        self.d = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.c = capacity
        self.l = 0

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.remove(node)
            self.push(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            self.remove(node)
            self.push(node)
            node.val = value
            return
        if self.l >= self.c:
            node = self.right.prev
            self.remove(node)
            self.d.pop(node.key)
            self.l -= 1
        self.l += 1
        new = Node(key, value)
        self.push(new)
        self.d[key] = new