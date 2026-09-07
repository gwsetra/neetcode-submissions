class Solution:
    # dutch flag algorithn
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lt = 0
        eq = 0
        gt = len(nums)-1
        pivot = 1

        while eq <= gt:
            if nums[eq] == pivot:
                # print('eq')
                eq += 1
            elif nums[eq] < pivot:
                # print('smaller', nums[eq], pivot)
                tmp = nums[lt]
                nums[lt] = nums[eq]
                nums[eq] = tmp
                lt += 1
                eq += 1
            elif nums[eq] > pivot:
                # print('bigger', nums[eq], pivot)
                tmp = nums[gt]
                nums[gt] = nums[eq]
                nums[eq] = tmp
                gt -= 1
            # print(nums)
        