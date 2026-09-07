class Solution:
    # sorting solution
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numlen = len(nums)-1
        lp = 1
        rp = numlen
        nums.sort()
        res = []
        print(nums)

        for i in range(0, numlen-1):
            if i > 0:
                if nums[i] == nums[i-1]:
                    # print('same first element found')
                    continue
            lp = i + 1
            rp = numlen
            loop = 0
            while lp < rp:
                tmp = nums[i] + nums[lp] + nums[rp]
                if tmp == 0:
                    res.append([nums[i], nums[lp], nums[rp]])
                    rp -= 1
                    while nums[rp] == nums[rp+1] and rp > i:
                        # print(rp)
                        rp -= 1 

                    lp += 1
                    while nums[lp] == nums[lp-1] and lp < numlen:
                        # print(lp)
                        lp += 1
                # print(tmp)
                elif tmp > 0:
                    rp -= 1
                elif tmp < 0:
                    lp += 1
                loop += 1
        return res