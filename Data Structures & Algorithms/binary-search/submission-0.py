import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        loops = 1

        while loops < 10:
            middle = math.floor((left + right)/2)
            print("left", left)
            print("right", right)
            print("middle", middle)
            print(nums[middle])
            print(target)

            if left > right:
                return -1
            
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1

            