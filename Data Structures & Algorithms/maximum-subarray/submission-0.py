class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestsum = -math.inf
        cursum = 0
        for num in nums:
            # print(num)
            if cursum < 0:
                cursum = 0
            print('***')
            print(largestsum, cursum)
            cursum += num


            largestsum = max(largestsum, cursum)
            print(largestsum, cursum)
        return largestsum