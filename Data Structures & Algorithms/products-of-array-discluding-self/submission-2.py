class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # best solution
        pref = [0]*len(nums)
        curr = [0]*len(nums)
        suff = [0]*len(nums)
        numslen = len(nums)

        pref[0] = 1
        suff[numslen-1] = 1

        for item in range(1, numslen, 1):
            pref[item] = nums[item-1] * pref[item-1]

        for item2 in range(numslen-2, -1, -1):
            # print('inside item2')
            # print(item2)
            suff[item2] = nums[item2+1] * suff[item2+1]
        
        for item in range(numslen):
            curr[item] = pref[item] * suff[item]
        
        return curr