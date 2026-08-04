class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        r=1

        for idx in range(len(nums)):
            print(l, r)
            if nums[l] == nums[r] and abs(l-r) <=k:
                return True
            if r-l > k:
                l += 1
                continue
            r += 1
        # print(l, r)
        return False