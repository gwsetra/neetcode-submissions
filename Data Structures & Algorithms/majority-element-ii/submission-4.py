class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maps = defaultdict(int)
        res = []

        for i in range(len(nums)):
            maps[nums[i]] +=1

        for item, ocur in maps.items():
            # print(ocur, (i/3) ,ocur/i > (i/3))
            if ocur > ((i+1)/3):
                res.append(item)
        return res