class Solution:
    # using while
    def searchInsert(self, nums: List[int], target: int) -> int:
        si = 0
        ei = len(nums)
        mid = ((ei-si) // 2) + si
        print(mid, ei)
        
        while si < ei:
            print('***')
            print(si, mid, ei, target, nums[mid-1])
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                print('target is smaller than mid')
                ei = mid
            elif target > nums[mid]:
                print('target is bigger than mid')
                si = mid + 1
            mid = ((ei-si) // 2) + si
            print(si, mid, ei, target, nums[mid-1])
        print(si, mid, ei)


        return si