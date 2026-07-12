class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []
        for li in points:
            dist = (li[0] ** 2) + (li[1] ** 2)
            res.append((dist, [li[0], li[1]]))

        heapq.heapify(res)
        ans = []
        print(res)
        while k > 0:
            ans.append(heapq.heappop(res)[1])
            k-=1
        return ans

        