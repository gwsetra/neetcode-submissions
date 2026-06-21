class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # print(nums)
        # print(target)
        tmptarget=target

        for loop, items in enumerate(nums):
            tmptarget=target
            print(loop, items)
            tmptarget -= items
            print(tmptarget)
            # print(nums[loop:])
            if tmptarget in nums[loop+1:]:
                print('FOUND')
                print(loop, nums.index(tmptarget, loop+1))
                return [loop, nums.index(tmptarget, loop+1)]