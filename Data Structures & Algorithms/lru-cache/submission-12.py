class Node:

    def __init__(self, key= 0,val = 0):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.d = {}

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.remove(node)
            self.addleft(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            if len(self.d) == self.c:
                r = self.right.prev
                self.d.pop(r.key)
                self.remove(r)
            self.d[key] = Node(key,value)
        else:
            self.d[key].val = value
            self.remove(self.d[key])
        
        self.addleft(self.d[key])


                
    
    def addleft(self, node):
        second = self.left.next
        self.left.next = node
        node.prev = self.left
        node.next = second
        second.prev = node

    def remove(self, node):
        bef = node.prev
        new = node.next
        bef.next = new
        new.prev = bef
        
