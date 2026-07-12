"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cur = Node(node.val)
        seen = set()
        d = {node: cur}
        def dfs(node, cur):
            print(node.val)
            if node in seen:
                return
            seen.add(node)
            for i in node.neighbors: 
                if i not in d:
                    d[i] = Node(i.val)
                temp = d[i]
                cur.neighbors.append(temp)
                dfs(i, temp)
                
            return cur
        return dfs(node, cur)

            