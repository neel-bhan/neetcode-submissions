class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:


    def __init__(self, capacity: int):
        self.k = capacity
        self.d = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        if key in self.d:
            node =  self.d[key]
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev
            temp = self.left.next
            self.left.next = node
            node.prev = self.left
            node.next = temp
            temp.prev = node
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.d:
            node =  self.d[key]
            node.val = value
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev
        else:
            node = Node(key, value)
            self.d[key] = node
        temp = self.left.next
        self.left.next = node
        node.prev = self.left
        node.next = temp
        temp.prev = node
        node.val = value
        if len(self.d) > self.k:
            node = self.right.prev
            prev = node.prev
            prev.next = self.right
            self.right.prev = prev
            self.d.pop(node.key)

        
