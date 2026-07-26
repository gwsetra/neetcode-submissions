class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        isloop = False
        largestsum = -math.inf
        cursum = -math.inf
        cur = 0
        loop = 0

        while True and loop <10:
            print(' *** ')
            if cursum < largestsum and isloop:
                return largestsum
            elif cursum < 0:
                cursum = 0
            print(largestsum, cursum)
            
            cursum += nums[cur]
            
            if cur+1 == len(nums): # move pointer to beginning
                cur = 0
                isloop = True
                continue
            
            largestsum = max(largestsum, cursum)
            print(largestsum, cursum)
            loop += 1
            cur += 1
        
        return largestsum