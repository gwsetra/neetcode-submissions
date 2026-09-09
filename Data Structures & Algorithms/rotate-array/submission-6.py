class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums) if k > len(nums) else k
        if k == 0:
            nums[:] = nums
        else:
            print(nums[-k:], nums[:len(nums)-k])
            nums[:] = nums[-k:] + nums[:len(nums)-k]