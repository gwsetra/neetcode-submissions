class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keyval = []
        for item in nums:
            if item in keyval:
                return True
            else:
                keyval.append(item)
        return False