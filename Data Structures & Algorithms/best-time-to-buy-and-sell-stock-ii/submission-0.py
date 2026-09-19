class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        movingsum = 0

        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                movingsum += prices[i+1]-prices[i]

        return movingsum
                