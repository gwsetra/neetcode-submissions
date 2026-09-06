class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        print(target)

        def findsub( si, ei):
            print('inside findsub', si, ei)
            mid = ((ei-si) // 2) + si
            print(mid)

            if target == mid:
                print('exact element match found')
                return mid
            
            if si == ei:
                print('si == ei')
                print(nums[ei], target)
                if target <= nums[ei] :
                    return ei
                
                return ei+1

            elif target < nums[mid]:
                print('target < mid', target, nums[mid])
                return findsub(si, mid)
            
            elif target > nums[mid]:
                print('target > mid', target, nums[mid])
                return findsub(mid+1, ei)
        
        return findsub(0, len(nums)-1)
