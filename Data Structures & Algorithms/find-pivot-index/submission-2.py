class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        leftsum = 0
        rightsum = 0
        # print(totalsum)

        for idx in range(len(nums)):
            # print('***')
            # print(idx)
            if idx == 0:
                rightsum = totalsum
            elif idx == len(nums):
                leftsum = totalsum
            else:
                leftsum += nums[idx-1]
            # print(leftsum)
            # print(totalsum, nums[idx], leftsum)
            # print(totalsum-nums[idx]-leftsum)
            if leftsum == totalsum-nums[idx]-leftsum:
                return idx
        return -1