class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        defs = defaultdict(int)
        biggest = -1

        for i in range(len(nums)):
            defs[nums[i]] +=1

        for item in defs.items():
            if item[1] > 1:
                continue
            biggest = max(biggest, item[0])
        # print(defs)
        return biggest