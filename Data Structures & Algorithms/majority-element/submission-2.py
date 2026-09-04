class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maps = defaultdict(int)
        mostfreq = 0

        for i in range(len(nums)):
            maps[nums[i]] += 1
        

        print(maps)
        return max(maps, key=maps.get)