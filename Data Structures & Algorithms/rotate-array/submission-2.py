class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums[-k:], nums[:k+1])
        nums[:] = nums[-k:] + nums[:k+1]