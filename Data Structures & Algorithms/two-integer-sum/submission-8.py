class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # print(nums)
        # print(target)
        tmptarget=target

        for loop, items in enumerate(nums):
            tmptarget=target
            tmptarget -= items
            if tmptarget in nums[loop+1:]:
                return [loop, nums.index(tmptarget, loop+1)]