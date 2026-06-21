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

            while left < right:
                tmph = h
                middle = (left+right)//2
                print(left, middle, right)

                for loop in range(len(piles)-1):
                    print(piles[loop], tmph)
                    tmph -= (piles[loop] // middle) + 1
                    print(piles[loop], tmph)
                
                if tmph > 0:
                    print('inside tmph')
                    right = middle
                    tmpresult = middle
                else:
                    left = middle + 1
                iters += 2
            return tmpresult