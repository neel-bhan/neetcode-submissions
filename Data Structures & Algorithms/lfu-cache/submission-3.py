class Node:

    def __init__(self, key, val):
        self.val  = val
        self.key = key
        self.prev = None
        self.next = None
        self.freq = 1

class LinkedList:

    def __init__(self):
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def length(self):
        return self.size

    def pushRight(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.size += 1

    def pop(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        node.prev = None
        node.next = None
        self.size -= 1

    def popLeft(self):
        if self.length() == 0:
            return None
        node = self.left.next
        self.pop(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0
        self.nodeMap = {}
        self.listMap = defaultdict(LinkedList)
    
    def update(self, node):
        node_count = node.freq
        self.listMap[node_count].pop(node)

        if node_count == self.lfuCnt and self.listMap[node_count].length() == 0:
            self.lfuCnt += 1
        
        node.freq += 1
        self.listMap[node.freq].pushRight(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.update(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node  = self.nodeMap[key]
            node.val = value
            self.update(node)
        else:
            if len(self.nodeMap) == self.cap:
                delete = self.listMap[self.lfuCnt].popLeft()
                self.nodeMap.pop(delete.key)
            self.lfuCnt = 1
            add = Node(key, value)
            self.listMap[1].pushRight(add)
            self.nodeMap[key] = add
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)