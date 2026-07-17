class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [] 
        for idx,item in enumerate(nums):
            # print(idx, item)
            copy = nums[:idx] + nums[idx+1:]
            # print(copy)
            # print(math.prod(copy))
            res.append(math.prod(copy))
        # print(res)
        return res