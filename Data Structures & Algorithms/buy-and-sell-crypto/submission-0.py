class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        ans = 0
        buy, sell = prices[0], prices[0]
        while r < len(prices):
            if prices[r] < buy:
                buy = prices[r]
            ans = max(ans, prices[r] - buy)
            r+=1
        return ans
            
