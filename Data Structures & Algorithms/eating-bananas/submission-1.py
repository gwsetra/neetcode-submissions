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
            middle = (left+right)//2
            print(left, middle, right)
            iters = 0
            tmpresult = None

            while left < right and iters < 10:
                tmph = h
                middle = (left+right)//2
                print(left, middle, right)

                for loop in range(len(piles)):
                    print(piles[loop], tmph)
                    tmph -= piles[loop] // middle + 1
                    print(tmph)
                
                if tmph > 0:
                    right = middle
                    tmpresult = middle
                else:
                    left = middle + 1
                iters += 2
            return tmpresult