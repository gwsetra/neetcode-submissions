class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lp=1
        rp=2
        cp=0
        numlen = len(nums)-1
        res = []

        while cp < numlen-1:
            for i in range(cp+1, numlen, 1):
                for n in range(i+1, numlen+1, 1):
                    # print(cp, i, n)
                    if nums[cp]+nums[i]+nums[n] == 0:
                        # print([nums[cp], nums[i], nums[n]])
                        tmp = [nums[cp], nums[i], nums[n]]
                        tmp.sort()
                        if tmp not in res:
                            res.append(tmp)
            cp+=1
        # print(res)
        return res