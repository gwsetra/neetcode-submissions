class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        self.prefixsum = defaultdict(int)
        print(self.prefixsum)
        self.cursum = 0
        count = 0
        
        self.prefixsum[0] = 1
        for i in range(len(nums)):
            self.cursum += nums[i]
            prevsum = self.cursum - k

            if prevsum in self.prefixsum:
                count += self.prefixsum[prevsum]

            self.prefixsum[self.cursum] += 1
            
        return count