class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        r=0
        sets = set()

        if k == 0:
            return False

        for idx in range(len(nums)):
            # print(l, r)
            # print(nums[l], nums[r])
            # print('sets', sets)
            if nums[idx] not in sets:
                sets.add(nums[idx])

                if idx >= k:
                    sets.remove(nums[idx-k])
            else:
                return True
        return False