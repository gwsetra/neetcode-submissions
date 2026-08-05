class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cursum = 0
        l = 0
        r = 0
        maxlen = math.inf
        numlen = len(nums)

        while  r < numlen:
            # print('l r', l, r)
            cursum += nums[r]
            # print('cursum', cursum)
            if cursum >= target:
                while cursum >= target:
                    # print('cursum >. target')
                    maxlen = min(maxlen, r-l+1)
                    cursum -= nums[l]
                    l += 1
            r += 1
        return 0 if maxlen == math.inf else maxlen