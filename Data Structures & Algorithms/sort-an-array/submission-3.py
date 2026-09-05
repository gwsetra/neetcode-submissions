class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # print('**')
        # print(nums)
        numlen = len(nums)
        
        if numlen == 0:
            # print('reach end')
            return []
        if numlen == 1:
            # print('reach end')
            return nums
        
        pivot = nums[numlen-1]

        # print('pivot', pivot)

        ptr = 0 # moving right ptr
        idx = 0 # moving right for replacement
        while ptr < numlen:
            if nums[ptr] <= pivot:
                tmp = nums[idx]
                nums[idx] = nums[ptr]
                nums[ptr] = tmp
                idx += 1
            
            ptr += 1
        
        # print('after split')
        # print(nums[0:idx-1], nums[idx-1:idx], nums[idx:])
        # print('123213')
        res = (self.sortArray(nums[0:idx-1]) or []) + (nums[idx-1:idx] or []) + (self.sortArray(nums[idx:]) or [])
        # print('result:', res)

        return res