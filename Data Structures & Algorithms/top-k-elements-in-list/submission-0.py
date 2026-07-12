class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        ans = []
        for key, v in d.items():
            ans.append((v, key))
        ans.sort()
        ret = []
        for i in range(-k, 0):
            print(i)
            ret.append(ans[i][1])
        return ret    

