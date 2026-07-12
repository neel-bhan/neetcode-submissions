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

        d = {}
        def dfs(node):
            if node in d:
                return d[node]
            copy = Node(node.val)
            d[node] = copy
            for c in node.neighbors:
                copy.neighbors.append(dfs(c))
                
            return copy
        return dfs(node)

            