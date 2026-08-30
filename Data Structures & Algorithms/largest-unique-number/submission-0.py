class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        defs = set()

        for i in range(len(nums)):
            if nums[i] not in defs:
                defs.add(nums[i])
            else:
                defs.remove(nums[i])
        
        # print(max(defs))
        return -1 if len(defs) == 0 else max(defs)