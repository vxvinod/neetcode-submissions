class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i, buy in enumerate(prices):
            for sell in prices[i+1:]:
                max = (sell - buy) if(sell-buy > max) else max
        return max