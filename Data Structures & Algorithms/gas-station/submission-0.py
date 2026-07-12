class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        visit = 0
        gass = 0
        cur = 0
        res = 0
        while True:
            if cur >= len(gas):
                cur = cur %len(gas)
            if res > len(gas) - 1:
                return -1

            gass += gas[cur] - cost[cur]
            if gass < 0:
                gass = 0
                visit = 0
                res += 1
                cur = res
                continue
            
            visit += 1
            cur += 1
            if visit == len(gas):
                return res
            
                
            
        