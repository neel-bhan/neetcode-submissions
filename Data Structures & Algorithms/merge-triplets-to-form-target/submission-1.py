class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        
        for a, b, c in triplets:
            if target[0] >= 0:
                if a == target[0] and b <= abs(target[1]) and c <= abs(target[2]):
                    target[0]*= -1
            if target[1] >= 0:
                if b == target[1] and a <= abs(target[0]) and c <= abs(target[2]):
                    target[1]*= -1    
            if target[2] >= 0:
                if c == target[2] and b <= abs(target[1]) and a <= abs(target[2]):
                    target[2]*= -1
        for t in target:
            if t >= 0:
                return False
        return True
