class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keyval = set()
        for item in nums:
            if item in keyval:
                return True
            else:
                keyval.add(item)
        return False