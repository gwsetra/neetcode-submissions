class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minval = min(len(piles), h)
        print(minval)

        maxval = -1
        for x in range(len(piles)):
            if piles[x] > maxval:
                maxval = piles[x]
        print(maxval)

        if h == len(piles):
            return maxval
        else: # find minimum value
            left = 0
            right = maxval

            return h//maxval
