class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        l=0
        r=1
        while r<len(prices):
            if prices[r]-prices[l]<0:
                l+=1
                r+=1
            else:
                maxprofit+=prices[r]-prices[l]
                r+=1
                l+=1
        return maxprofit
                