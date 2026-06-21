class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slowpointer = fastpointer = 1
        while fastpointer < len(nums)-1:
            fastpointer += 1
            if nums[slowpointer-1] != nums[fastpointer]:
                nums[slowpointer] = nums[fastpointer]
                slowpointer += 1
        return slowpointer
