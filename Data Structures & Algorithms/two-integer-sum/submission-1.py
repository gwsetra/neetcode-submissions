class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # print(nums)
        # print(target)
        tmptarget=target

        for loop, items in enumerate(nums):
            tmptarget -= items

            if tmptarget in nums[loop:]:
                # print('FOUND')
                # print(loop, nums.index(tmptarget))
                return [loop, nums.index(tmptarget)]