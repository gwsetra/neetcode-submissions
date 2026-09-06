class Solution:
    # 3-way quick sort
    def sortArray(self, nums: List[int]) -> List[int]:
        # print('**')
        # print(nums)

        lennums = len(nums)
        lp = 0
        ep = 0
        gp = lennums-1
        cur = 0

        if lennums <= 1:
            return nums

        pivotnum = nums[lennums//2]
        # print(pivotnum)

        while ep <= gp:
            # print(nums)
            # print(lp, ep, gp)
            # smaller case
            if nums[ep] < pivotnum:
                # print('smaller case')
                tmp = nums[lp]
                nums[lp] = nums[ep]
                nums[ep] = tmp 
                lp += 1
                ep += 1

            # equal case
            elif nums[ep] == pivotnum:
                # print('equal case')
                ep += 1
            # bigger case
            elif nums[ep] > pivotnum:
                # print('bigger case')
                tmp = nums[gp]
                nums[gp] = nums[ep]
                nums[ep] = tmp 
                gp -= 1
            # print(lp, ep, gp)
        
        # print(nums)
        # print(nums[:lp], nums[lp:ep], nums[ep:])
        return((self.sortArray(nums[:lp]) or []) + (nums[lp:ep] or []) + (self.sortArray(nums[ep:]) or []))
        # print(nums)