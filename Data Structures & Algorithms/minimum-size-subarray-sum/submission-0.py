class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cursum = 0
        l = 0
        r = 0
        maxlen = 0

        while l != len(nums)-1 and r != len(nums)-1:
            cursum += nums[r]
            # print('cursum', cursum)
            if cursum >= target:
                # print('resett')
                maxlen = (r-l)+1
                l += 1
                r = l
                cursum = 0
                # print('l r', l, r)
                continue
            r += 1
        return maxlen