class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cursum = 0
        l = 0
        r = 0
        maxlen = math.inf
        numlen = len(nums)

        while l != numlen:
            if r == numlen:
                l += 1
                r = l
                cursum = 0
                # print('l r', l, r)
                continue
            cursum += nums[r]
            # print('cursum', cursum)
            if cursum >= target:
                # print('resett')
                # print((r-l)+1)
                maxlen = min(maxlen, (r-l)+1)
                l += 1
                r = l
                cursum = 0
                # print('l r', l, r)
                continue
            r += 1
        return 0 if maxlen == math.inf else maxlen