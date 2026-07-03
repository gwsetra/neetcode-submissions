class Solution:
    def rob(self, nums: List[int]) -> int:
        is_even = (len(nums) % 2) == 0
        max_odd = 0
        max_even = 0

        for i in range(len(nums)):
            # print(i)
            if i % 2 == 0:
                max_even += nums[i]
            else:
                max_odd += nums[i]
        print(max_odd, max_even)
        return max_even if max_even >= max_odd else max_odd