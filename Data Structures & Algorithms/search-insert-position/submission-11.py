class Solution:
    # using while
    def searchInsert(self, nums: List[int], target: int) -> int:
        si = 0
        ei = len(nums)-1
        mid = ((ei-si) // 2) + si
        
        while mid < ei:
            print('***')
            mid = ((ei-si) // 2) + si
            print(si, mid, ei, target, nums[mid])
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                print('target is smaller than mid')
                ei = mid-1
            elif target > nums[mid]:
                print('target is bigger than mid')
                si = mid + 1
            print(si, mid, ei, target, nums[mid])
        print(si, mid, ei)

        if si == len(nums):
            return si
        elif ei == 0:
            return 0
        return mid 