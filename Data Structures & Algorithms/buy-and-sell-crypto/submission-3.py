class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        res =0 
        for i in prices:
            buy = min(buy, i)
            res = max(res,i - buy)
        return res
