class Solution:
    # sorting solution
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numlen = len(nums)-1
        lp = 1
        rp = numlen
        nums.sort()
        res = []

        for i in range(0, numlen-1):
            lp = i + 1
            rp = numlen
            loop = 0
            while lp < rp:
                tmp = nums[i] + nums[lp] + nums[rp]
                if tmp == 0:
                    res.append([nums[i], nums[lp], nums[rp]])
                    break
                # print(tmp)
                if tmp > 0:
                    rp -= 1
                elif tmp < 0:
                    lp += 1
                loop += 1
        return res