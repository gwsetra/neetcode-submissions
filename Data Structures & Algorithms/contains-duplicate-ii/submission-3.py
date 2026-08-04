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
            else:
                while True:
                    # print('inside True')
                    # print(nums[l] == nums[r])
                    # print(abs(l-r) <= k)
                    if nums[l] == nums[r] and abs(l-r) <= k:
                        return True
                    else:
                        l+=1
                        if l == len(nums) or l==r:
                            break
            r += 1
        return False