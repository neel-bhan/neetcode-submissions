class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sum = 0
        subset = []
        res = []
        candidates.sort()


        

        print(candidates)
        def dfs(i, sum ):
            if sum == target:
                res.append(subset.copy())
                return
            if sum > target or i >= len(candidates):
                return
            
            subset.append(candidates[i])
            dfs(i+1, sum + candidates[i])
            subset.pop()
            while True:
                if i + 1 >= len(candidates):
                    return
                if candidates[i+1] == candidates[i]:
                    i += 1
                    print('here')
                    continue
                
                break
            dfs(i+1, sum)
        dfs(0,0)
        return res