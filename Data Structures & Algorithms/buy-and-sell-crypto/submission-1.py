class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mins = math.inf
        minsidx = None
        diffs = -math.inf

        for r in range(len(prices)):
            if prices[r] < mins:
                minsidx = r
            mins = min(mins, prices[r])

            if prices[r] > mins:
                diffs = max(diffs, prices[r] - mins)
            # print(mins, diffs)
        return 0 if diffs == -math.inf else diffs