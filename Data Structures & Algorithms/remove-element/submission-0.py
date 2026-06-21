class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        sp = fp = 0
        for loop in range(len(nums)):
            if nums[fp] == val:
                fp += 1
            else:
                nums[sp] = nums [fp]
                sp += 1
                fp +=1
        return sp