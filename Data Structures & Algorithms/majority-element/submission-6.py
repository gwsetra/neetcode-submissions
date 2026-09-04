class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curelem = None
        cnt = None

        for i in range(len(nums)):
            if curelem == None and cnt == None:
                curelem = nums[i]
                cnt = 1
                continue
            
            cnt += 1 if (curelem == nums[i]) else -1 


            if cnt == 0:
                curelem = None
                cnt = None

        return curelem
            
