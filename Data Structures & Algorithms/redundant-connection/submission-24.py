class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = {}
        def find(p):
            ori = p
            while p in d:
                p = d[p]
            if p != ori:
                d[ori] = p
            return p
        
        def union(p1, p2):
            f1, f2 = find(p1), find(p2)
            if f1 == f2:
                return False
            d[f1] = f2
            return True
        res = [0,0]
        for i, j in edges:
            if not union(i, j):
                res =  [i,j]
        return res

        